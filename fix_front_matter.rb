#!/usr/bin/env ruby

# Path to the courses directory
courses_dir = '_courses'

# Process each course file
Dir.glob("#{courses_dir}/*.md").each do |file_path|
  puts "Processing: #{file_path}"
  
  # Read the file content
  content = File.read(file_path)
  
  # Check if the file has duplicate front matter markers (---)
  if content =~ /\A---\s*\n---\s*\n/
    puts "  Found duplicate front matter markers, fixing..."
    
    # Fix the duplicate front matter markers
    new_content = content.sub(/\A---\s*\n---\s*\n/, "---\n")
    
    # Write the updated content back to the file
    File.write(file_path, new_content)
    puts "  Fixed front matter format"
  else
    puts "  Front matter format is already correct"
  end
end

puts "Finished processing all course files." 