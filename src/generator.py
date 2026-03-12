from converter import markdown_to_html_node
import os


def extract_title(markdown):
        title_found = False
        for line in markdown.splitlines():
            if line.startswith('# '):
                title_found = True
                return line[2:].strip()
        if not title_found:
            raise Exception("No title found in the provided markdown content.")
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    title = extract_title(markdown_content)
    with open(template_path, 'r') as f:
        template_content = f.read()
    html_string = markdown_to_html_node(markdown_content).to_html()
    page_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_string)
    #write the page content to the destination path and create any necessary directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(page_content)

def generate_pages_recursive(dir_path_content, template_path, dir_path_dest):
    print(f"This script is in directory: {os.path.dirname(__file__)}")
    for entry in os.listdir(dir_path_content):
        content_entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dir_path_dest, entry.replace('.md', '.html'))
        if os.path.isdir(content_entry_path):
            generate_pages_recursive(content_entry_path, template_path, dest_entry_path)
        elif content_entry_path.endswith('.md'):
            generate_page(content_entry_path, template_path, dest_entry_path)
    