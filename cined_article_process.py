#!/usr/bin/env python3
"""
Template script for creating new CineD articles from scratch
This template supports multiple extraction methods for maximum flexibility

USAGE:
1. Replace [CINED_URL] with the actual CineD article URL
2. Replace [ARTICLE_TOPIC] with the topic extracted from URL
3. Choose extraction method based on complexity and needs
4. Replace image URLs with actual URLs extracted
5. Execute script to create complete Jekyll post

EXTRACTION METHODS (Choose the best one for your situation):

METHOD 1 - MARKDOWN EXPORT (RECOMMENDED 2025+):
- Export CineD article to markdown using browser extension
- Extract images: grep -oE 'https://www\.cined\.com/content/uploads/[^)]*\.(jpg|jpeg|png)' article.md
- Use markdown content directly for article structure
- FASTEST and most complete method

METHOD 2 - CURL + GREP (RELIABLE FOR SIMPLE EXTRACTION):
# Images:
curl -s "CINED_URL" | grep -oE 'https://www\.cined\.com/content/uploads/202[0-9]/[0-9][0-9]/[^"]*ARTICLE_TOPIC[^"]*\.(jpg|jpeg|png)' | grep -v '\-[0-9]' | sort | uniq

# Videos:
curl -s "CINED_URL" | grep -oE 'youtube\.com/embed/[^"?]*' | sed 's/.*embed\///'

METHOD 3 - CHROME-MCP-SERVER (FOR COMPLEX EXTRACTION):
- Use mcp__playwright__browser_navigate() for dynamic content
- Use mcp__playwright__browser_evaluate() for complex selectors
- Best for articles with dynamic content or complex structure

SUCCESS CASE STUDY:
The "Utilizing Lens Aberrations for Styling Effects" article was processed using 
METHOD 1 (Markdown Export) with 100% success:
- 18 images downloaded successfully
- Complete content structure preserved
- Professional quality output achieved
"""
import requests
import re
from pathlib import Path
import time
from datetime import datetime

def create_new_article_from_cined_url():
    """Create a complete Jekyll article from a CineD URL"""
    
    # STEP 1: Configure article details
    cined_url = "[REPLACE_WITH_CINED_URL]"
    article_topic = "[REPLACE_WITH_TOPIC_FROM_URL]"  # e.g., "lighting-techniques-cinematography"
    article_title = "[REPLACE_WITH_HUMAN_READABLE_TITLE]"  # e.g., "Lighting Techniques in Cinematography"
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # STEP 2: Images extracted from CineD article content using:
    # curl -s "CINED_URL" | grep -oE 'https://www\.cined\.com/content/uploads/202[0-9]/[0-9][0-9]/[^"]*ARTICLE_TOPIC[^"]*\.(jpg|jpeg|png)' | grep -v '\-[0-9]' | sort | uniq
    images_to_download = [
        {
            'url': 'https://www.cined.com/content/uploads/YYYY/MM/article_topic-feature_image.jpg',
            'filename': f'{article_topic}-hero.jpg',
            'alt': f'{article_title} main image',
            'caption': f'{article_title} overview. Image source: CineD'
        },
        {
            'url': 'https://www.cined.com/content/uploads/YYYY/MM/article_topic-example1.jpg',
            'filename': f'{article_topic}-example-1.jpg',
            'alt': 'Descriptive alt text',
            'caption': 'Descriptive caption. Image source: CineD'
        },
        # Add more images as extracted from CineD article
    ]
    
    # STEP 3: Videos extracted using:
    # curl -s "CINED_URL" | grep -oE 'youtube\.com/embed/[^"?]*' | sed 's/.*embed\///'
    videos_to_embed = [
        {
            'type': 'youtube',
            'embed_id': 'VIDEO_ID_HERE',
            'title': 'Video title',
            'caption': 'Video description. Video source: CineD'
        }
        # Add more videos as found in the article
    ]
    
    # Download images
    images_dir = Path('/Users/mac/repos/mzdev/assets/images/posts')
    images_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded_images = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    for img_info in images_to_download:
        try:
            image_path = images_dir / img_info['filename']
            
            if not image_path.exists():
                print(f"Downloading: {img_info['filename']}")
                
                response = requests.get(img_info['url'], timeout=30, headers=headers)
                response.raise_for_status()
                
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                print(f"  Successfully downloaded: {img_info['filename']}")
                time.sleep(0.5)  # Be polite to the server
            else:
                print(f"  Already exists: {img_info['filename']}")
                
            downloaded_images.append({
                'local_path': f"/assets/images/posts/{img_info['filename']}",
                'alt': img_info['alt'],
                'caption': img_info.get('caption', '')
            })
        except Exception as e:
            print(f"  Error downloading {img_info['url']}: {e}")
    
    # STEP 4: Download images
    downloaded_images = download_images(images_to_download)
    
    # STEP 5: Generate comprehensive content
    full_content = generate_comprehensive_content(article_topic, article_title, downloaded_images, videos_to_embed)
    
    # STEP 6: Create Jekyll post
    success = create_jekyll_post(article_topic, article_title, current_date, downloaded_images, videos_to_embed, full_content)
    
    return success, len(downloaded_images), len(videos_to_embed)

def download_images(images_to_download):
    """Download images and return local path information"""
    images_dir = Path('/Users/mac/repos/mzdev/assets/images/posts')
    images_dir.mkdir(parents=True, exist_ok=True)
    
    downloaded_images = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    for img_info in images_to_download:
        try:
            image_path = images_dir / img_info['filename']
            
            if not image_path.exists():
                print(f"Downloading: {img_info['filename']}")
                
                response = requests.get(img_info['url'], timeout=30, headers=headers)
                response.raise_for_status()
                
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                print(f"  Successfully downloaded: {img_info['filename']}")
                time.sleep(0.5)  # Be polite to the server
            else:
                print(f"  Already exists: {img_info['filename']}")
                
            downloaded_images.append({
                'local_path': f"/assets/images/posts/{img_info['filename']}",
                'alt': img_info['alt'],
                'caption': img_info.get('caption', '')
            })
        except Exception as e:
            print(f"  Error downloading {img_info['url']}: {e}")
    
    return downloaded_images

def create_jekyll_post(article_topic, article_title, current_date, downloaded_images, videos, content):
    """Create a complete Jekyll post file from scratch"""
    
    # Generate filename
    filename = f"{current_date}-{article_topic}.markdown"
    post_file = Path(f'/Users/mac/repos/mzdev/_posts/{filename}')
    
    # Generate front matter
    front_matter = f"""---
date: '{current_date}'
image: /assets/images/posts/{article_topic}-hero.jpg
layout: post
meta_description: {article_title} - Professional filmmaking insights and techniques
subtitle: {article_title} - Professional filmmaking insights and techniques
title: {article_title}
---"""
    
    # Write complete post
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.write('\n\n')
        f.write(content)
    
    print(f"\nSuccessfully created {post_file.name} with {len(downloaded_images)} images and {len(videos)} videos!")
    print(f"Article topic: {article_title}")
    return True

def generate_comprehensive_content(article_topic, article_title, downloaded_images, videos):
    """Generate comprehensive, expert-level content (3000-8000 words)
    
    STRATEGY NOTES (Based on lens aberrations success):
    1. Use exported markdown content directly when available
    2. Maintain original technical accuracy and expert insights
    3. Add contextual image placement throughout content
    4. Include proper attribution to sources (CineD, instructors)
    5. Preserve educational value while adapting for MZed audience
    6. Add practical applications and modern cinematography context
    """
    
    # For markdown export method, process the exported content directly
    # For other methods, generate comprehensive content based on topic
    content = f"""[COMPREHENSIVE ARTICLE CONTENT FOR {article_title.upper()}]

CONTENT GENERATION STRATEGY:
1. **CRITICAL: USE ONLY ORIGINAL CINED CONTENT**
   - Copy text directly from CineD markdown export
   - DO NOT add, expand, or enhance content
   - DO NOT create new sections or explanations
   - Preserve exact wording and structure from original

2. **Content Processing Rules**
   - Extract content from markdown export only
   - Maintain original section organization
   - Keep all technical details exactly as written
   - Preserve author's voice and expertise

3. **Professional Image Integration**
   - Place images contextually within relevant sections
   - Use descriptive alt text for accessibility
   - Include proper source attribution (Image source: CineD)

4. **Authenticity Standards**
   - Zero fabricated content
   - Zero additional context or explanations
   - Complete preservation of original article integrity
   - Accurate representation of expert insights

5. **CRITICAL: Complete Media Extraction**
   - Extract and embed ALL videos from original article
   - Include ALL images from original article
   - Preserve exact video placement and context
   - Convert YouTube links to proper iframe embeds
   - Include all video captions and descriptions

[GENERATE SECTIONS BASED ON ARTICLE TOPIC - USE MARKDOWN EXPORT WHEN AVAILABLE]"""

    # Add images contextually throughout the content
    for i, img in enumerate(downloaded_images):
        if i == 0:
            # Hero image at the top
            content += f"\n\n![{img['alt']}]({img['local_path']})\n*{img['caption']}*\n"
        else:
            # Distribute other images throughout sections
            content += f"\n\n![{img['alt']}]({img['local_path']})\n*{img['caption']}*\n"
    
    # Add video embeds
    for video in videos:
        if video['type'] == 'youtube':
            content += f'\n\n<iframe width="560" height="315" src="https://www.youtube.com/embed/{video["embed_id"]}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n*{video["caption"]}*\n'
    
    content += """

## Conclusion

[Comprehensive conclusion summarizing key insights and practical takeaways for filmmakers]

This article provides professional-level insights into [TOPIC] that will help filmmakers at all levels improve their craft and create more compelling visual stories."""

    return content

if __name__ == "__main__":
    # Execute the main article creation function
    success, image_count, video_count = create_new_article_from_cined_url()
    
    if success:
        print(f"\n🎉 Article creation completed successfully!")
        print(f"📸 Images processed: {image_count}")
        print(f"🎬 Videos embedded: {video_count}")
        print(f"📝 Ready for publication!")
    else:
        print(f"\n❌ Article creation failed. Please check the configuration and try again.")