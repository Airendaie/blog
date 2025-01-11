import os
import json
import markdown
from datetime import datetime

def update_index_json():
    posts_dir = 'posts'
    posts = []
    
    # Get all markdown files
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(posts_dir, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert markdown to HTML
            html_content = markdown.markdown(content)
            
            # Get file creation time for sorting
            file_stats = os.stat(file_path)
            creation_time = datetime.fromtimestamp(file_stats.st_ctime)
            
            # Create post object
            post = {
                'title': filename.replace('.md', '').replace('-', ' ').title(),
                'content': content,
                'html_content': html_content,
                'date': creation_time.strftime('%Y-%m-%d'),
                'filename': filename
            }
            
            posts.append(post)
    
    # Sort posts by date, newest first
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Write to index.json
    with open(os.path.join(posts_dir, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    update_index_json()
