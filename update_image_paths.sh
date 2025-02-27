#!/bin/bash

# Loop through all markdown files in the _courses directory
for file in _courses/*.md; do
  # Use sed to replace the image path pattern in the frontmatter
  # This replaces:
  # 1. "/courses/assets/images/" with "/assets/images/courses/"
  # 2. "\/courses\/assets\/images\/" with "\/assets\/images\/courses\/"
  # The second pattern handles escaped paths
  
  sed -i '' 's|image: "/courses/assets/images/|image: "/assets/images/courses/|g' "$file"
  sed -i '' 's|image: /courses/assets/images/|image: /assets/images/courses/|g' "$file"
  
  echo "Updated $file"
done

echo "All course files updated successfully!" 