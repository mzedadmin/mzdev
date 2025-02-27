#!/bin/bash

# Remove the entire courses directory since we've moved all assets to the assets directory
echo "Removing courses directory..."
rm -rf courses

# Remove redundant layout files
echo "Removing redundant layout files..."
rm -f _layouts/courses-original.html

# Ensure the script completes
echo "Cleanup completed successfully!" 