import json
import os
from datetime import datetime
import config  # Importing configuration settings.

# Load the data from the JSON file.
def load_data():
    with open(config.JSON_FILE_PATH, 'r') as file:
        return json.load(file)

# Format the date string into a readable format.
def format_date(date_string):
    if date_string:
        date_obj = datetime.fromisoformat(date_string.rstrip('Z'))
        return date_obj.strftime("%Y-%m-%d")
    return ""

# Format individual highlight into markdown format.
def format_highlight(highlight):
    text = highlight.get('text', '')
    highlighted_at = highlight.get('highlighted_at', '')
    readwise_url = highlight.get('readwise_url', '#')
    source_url = highlight.get('url', '#')
    note = highlight.get('note', '')
    date_markdown = f" (Highlighted on: >{format_date(highlighted_at)})" if highlighted_at else ""
    
    return (
        f"- {text}"
        f"{date_markdown},"
        f" Source: {source_url},"
        f" Note: {note},"
        f" Readwise URL: {readwise_url}\n\n"
    )

# Create and write the markdown content to a file.
def create_markdown_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as md_file:
        md_file.write(content)

# Main function to generate markdown files from loaded data.
def generate_markdown_files():
    try:
        data = load_data()
        os.makedirs(config.MARKDOWN_OUTPUT_DIR, exist_ok=True)  # Ensure the markdown output directory exists.

        for item in data:
            # Extracting relevant information from each item.
            source = item.get('source', 'Unknown').lower()
            title = item.get('title', 'Untitled').replace('/', '_')  # Sanitize title to be file-system friendly.
            cover_image_url = item.get('cover_image_url', '')
            author = item.get('author', 'Unknown Author')
            category = item.get('category', 'Unknown Category')
            source_url = item.get('source_url', 'Unknown Source URL')

            # Compile markdown content.
            markdown_content = f"# {title}\n\n"
            if cover_image_url:
                markdown_content += f"![]({cover_image_url})\n\n"
            markdown_content += (
                "### Metadata\n\n"
                f"- Author: {author}\n"
                f"- Full Title: {title}\n"
                f"- Source: {source.capitalize()}\n"
                f"- Source URL: {source_url}\n"
                f"- Category: #{category}\n\n"
                "### Highlights\n\n"
            )

            for highlight in item.get('highlights', []):
                markdown_content += format_highlight(highlight)

            # Define the markdown file path and create the file.
            markdown_filename = f"{title}.md"
            markdown_file_path = os.path.join(config.MARKDOWN_OUTPUT_DIR, source, markdown_filename)
            create_markdown_file(markdown_file_path, markdown_content)

            print(f"Markdown file created for: {title} ({source})")

    except FileNotFoundError:
        print(f"File not found: {config.JSON_FILE_PATH}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file")
