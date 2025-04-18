#!/usr/bin/env ruby
require 'yaml'

# Path to the courses directory
courses_dir = '_courses'

# Process each course file
Dir.glob("#{courses_dir}/*.md").each do |file_path|
  puts "Processing: #{file_path}"
  
  # Extract the filename without extension to use as slug
  filename = File.basename(file_path, '.md')
  slug = filename
  
  # Read the file content
  content = File.read(file_path)
  
  # Check if the file has front matter (between --- markers)
  if content =~ /\A---\s*\n(.*?)\n---\s*\n/m
    front_matter_content = $1
    
    # Parse the front matter as YAML
    begin
      front_matter = YAML.load(front_matter_content)
      
      # Skip if slug is already present
      if front_matter.has_key?('slug')
        puts "  Slug already exists: #{front_matter['slug']}"
        next
      end
      
      # Add the slug attribute
      front_matter['slug'] = slug
      
      # Convert back to YAML
      new_front_matter = front_matter.to_yaml
      
      # Replace the old front matter with the new one
      new_content = content.sub(/\A---\s*\n.*?\n---\s*\n/m, "---\n#{new_front_matter}---\n\n")
      
      # Write the updated content back to the file
      File.write(file_path, new_content)
      puts "  Added slug: #{slug}"
    rescue => e
      puts "  Error processing #{file_path}: #{e.message}"
    end
  else
    puts "  No front matter found in #{file_path}"
  end
end

puts "Finished processing all course files." 