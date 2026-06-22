#!/usr/bin/env python3
"""Extract unique Unsplash IDs, download images, replace URLs, and add shimmer CSS."""

import re
import os
import subprocess
import concurrent.futures
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE, 'images')
HTML_FILES = ['business.html', 'ecommerce.html', 'store.html', 'cafe.html', 'restaurant.html', 'corporate.html']

# Unsplash photo IDs contain hex chars AND dashes, e.g. 1518314916381-77a37c2a49ae
ID_PATTERN = r'[a-f0-9-]{20,}'

# ============================================================
# PHASE 1: Extract unique photo IDs
# ============================================================
all_ids = set()
for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    ids = re.findall(r'https://images\.unsplash\.com/photo-(' + ID_PATTERN + r')', content)
    all_ids.update(ids)

ids_sorted = sorted(all_ids)
print(f"Found {len(ids_sorted)} unique Unsplash photo IDs")

# ============================================================
# PHASE 2: Download images (8 parallel at a time)
# ============================================================
os.makedirs(IMAGES_DIR, exist_ok=True)

def download_image(pid):
    """Download a single image, return (pid, success, msg)"""
    url_primary = f"https://images.unsplash.com/photo-{pid}?w=800&dpr=2"
    url_fallback = f"https://images.unsplash.com/photo-{pid}?w=800"
    dest = os.path.join(IMAGES_DIR, f"img_{pid}.jpg")
    
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return (pid, True, "already exists")
    
    # Try primary URL first
    try:
        result = subprocess.run(
            ['curl', '-sL', '-o', dest, '-w', '%{http_code}', url_primary],
            capture_output=True, text=True, timeout=30
        )
        http_code = result.stdout.strip()
        size = os.path.getsize(dest) if os.path.exists(dest) else 0
        if http_code == '200' and size > 1000:
            return (pid, True, f"OK (primary, {size} bytes)")
        
        # Try fallback without dpr
        result = subprocess.run(
            ['curl', '-sL', '-o', dest, '-w', '%{http_code}', url_fallback],
            capture_output=True, text=True, timeout=30
        )
        http_code = result.stdout.strip()
        size = os.path.getsize(dest) if os.path.exists(dest) else 0
        if http_code == '200' and size > 1000:
            return (pid, True, f"OK (fallback, {size} bytes)")
        
        return (pid, False, f"failed (HTTP {http_code}, {size}b)")
    except Exception as e:
        return (pid, False, f"exception: {e}")

print("Downloading images (8 at a time)...")
successes = 0
failures = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(download_image, pid): pid for pid in ids_sorted}
    for future in concurrent.futures.as_completed(futures):
        pid, ok, msg = future.result()
        if ok:
            successes += 1
            print(f"  ✓ {pid}: {msg}")
        else:
            failures += 1
            print(f"  ✗ {pid}: {msg}")

print(f"\nDownload complete: {successes} succeeded, {failures} failed")

# ============================================================
# PHASE 3: Replace URLs in files
# ============================================================
print("\n--- Phase 3: Replacing URLs in files ---")

for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    
    original = content
    
    # Replace all unsplash URLs with local paths
    def replace_url(match):
        full_url = match.group(0)
        pid = match.group(1)
        return f'images/img_{pid}.jpg'
    
    content = re.sub(
        r'https://images\.unsplash\.com/photo-(' + ID_PATTERN + r')\?[^"\' >]*',
        replace_url,
        content
    )
    
    if content != original:
        with open(path, 'w') as f:
            f.write(content)
        # Count replacements
        replacements = sum(1 for _ in re.finditer(r'images/img_', content))
        print(f"  ✓ {fn}: URLs replaced (local refs: {replacements})")
    else:
        print(f"  ? {fn}: No changes made")

# ============================================================
# PHASE 4: Add shimmer CSS and remove background-color from img tags
# ============================================================
print("\n--- Phase 4: Adding shimmer CSS ---")

SHIMMER_CSS = '''
/* Shimmer loading animation for images */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
img {
  background: linear-gradient(90deg, #e0e0e0 25%, #f0f0f0 50%, #e0e0e0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}
'''

for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    
    # Remove style="background-color:#..." from img tags  
    content = re.sub(
        r'<img\s+style="background-color:#[^"]*"',
        '<img',
        content
    )
    # Handle background-color in style attribute alongside other styles
    content = re.sub(
        r'(<img)([^>]*?style="[^"]*?)background-color:#[A-Fa-f0-9]+;?\s*',
        r'\1\2',
        content
    )
    # Clean up empty or leading-trailing semicolons in style
    content = re.sub(r'style=";\s*"', 'style=""', content)
    content = re.sub(r'\s+style=""', '', content)
    # Also handle standalone background-color via inline style on img
    content = re.sub(r'style="background-color:#[^"]*"', '', content)
    
    # Insert shimmer CSS before the closing </head> tag
    if '</head>' in content:
        content = content.replace('</head>', f'{SHIMMER_CSS}\n</head>', 1)
    
    with open(path, 'w') as f:
        f.write(content)
    print(f"  ✓ {fn}: Shimmer CSS added, background-color removed")

# ============================================================
# VERIFICATION
# ============================================================
print("\n--- Verification ---")
unsplash_count = 0
for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    count = len(re.findall(r'unsplash\.com', content))
    if count > 0:
        urls = re.findall(r'https://images\.unsplash\.com/[^\s"\'<>]+', content)
        for u in urls:
            print(f"  REMAINING: {u[:80]}")
        print(f"  ✗ {fn}: {count} unsplash.com references remaining!")
    else:
        print(f"  ✓ {fn}: 0 unsplash.com references")
    unsplash_count += count

if unsplash_count == 0:
    print("\n✓ ALL CLEAN: No unsplash.com references remain in any file!")
else:
    print(f"\n✗ {unsplash_count} unsplash.com references still remain!")
    sys.exit(1)

print("\nDone!")
