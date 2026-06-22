#!/usr/bin/env python3
"""Remove small (failed) image downloads and verify everything."""
import os, re

BASE = '/home/elmon/projects/portfolio-showcase/showcase'
IMAGES_DIR = os.path.join(BASE, 'images')

# Remove files under 1KB (failed 404 downloads)
removed = 0
for f in os.listdir(IMAGES_DIR):
    path = os.path.join(IMAGES_DIR, f)
    if f.endswith('.jpg') and os.path.getsize(path) < 1000:
        os.remove(path)
        removed += 1
        print(f"Removed failed download: {f}")

print(f"\nCleaned up {removed} failed downloads")

# Count remaining
remaining = [f for f in os.listdir(IMAGES_DIR) if f.endswith('.jpg')]
total_size = sum(os.path.getsize(os.path.join(IMAGES_DIR, f)) for f in remaining)
print(f"Images remaining: {len(remaining)}")
print(f"Total size: {total_size / 1024 / 1024:.1f} MB")

# Verify no unsplash.com references
HTML_FILES = ['business.html', 'ecommerce.html', 'store.html', 'cafe.html', 'restaurant.html', 'corporate.html']
unsplash_total = 0
for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    count = len(re.findall(r'unsplash\.com', content))
    unsplash_total += count
    status = '✓' if count == 0 else '✗'
    print(f"{status} {fn}: {count} unsplash.com references")

print(f"\n{'✓ ALL CLEAN!' if unsplash_total == 0 else f'✗ {unsplash_total} REMAINING!'}")
