#!/bin/bash

# Remove nested folders after we've moved their contents
echo "Removing nested folders..."

# Remove the courses directory inside assets/css
rm -rf assets/css/courses

# Remove the courses directory inside assets/js
rm -rf assets/js/courses

echo "Nested folders removed successfully!" 