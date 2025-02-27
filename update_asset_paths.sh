#!/bin/bash

# Update references in _layouts/courses-original.html
sed -i '' 's|/courses/assets/fonts/|/assets/fonts/|g' _layouts/courses-original.html

# Update references in _includes/mzed_pro_section.html
sed -i '' 's|/courses/assets/icons/|/assets/icons/|g' _includes/mzed_pro_section.html

# Update references in _includes/pricing_section.html
sed -i '' 's|/courses/assets/icons/|/assets/icons/|g' _includes/pricing_section.html

# Update references in courses.markdown
sed -i '' 's|/courses/assets/icons/|/assets/icons/|g' courses.markdown

echo "All asset references updated successfully!" 