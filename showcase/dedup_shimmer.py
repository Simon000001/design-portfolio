#!/usr/bin/env python3
"""Deduplicate shimmer CSS blocks (first run + second run produced duplicates)."""
import re
import os

BASE = '/home/elmon/projects/portfolio-showcase/showcase'
HTML_FILES = ['business.html', 'ecommerce.html', 'store.html', 'cafe.html', 'restaurant.html', 'corporate.html']

# The duplicate block (from first run - uses img:not(.no-shimmer))
first_shimmer = '''/* Shimmer loading animation for images */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
img:not(.no-shimmer) {
  background: linear-gradient(90deg, #e0e0e0 25%, #f0f0f0 50%, #e0e0e0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

'''

for fn in HTML_FILES:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        content = f.read()
    
    original = content
    
    # Remove the first (duplicate) shimmer block (which uses :not(.no-shimmer))
    # The second one (uses plain `img`) is the keeper
    if first_shimmer in content:
        content = content.replace(first_shimmer, '', 1)
        print(f"  ✓ {fn}: Removed duplicate shimmer block")
    
    # Also clean up any double blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(path, 'w') as f:
        f.write(content)

print("\nDone deduplicating!")
