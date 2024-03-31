from block_markdown import markdown_to_html_node
import re
import os

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block_text in blocks:
        if block_text.startswith("# "):
            return block_text[2:].strip()
    raise Exception("Header not in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as from_file:
        from_contents = from_file.read()
    with open(template_path) as template_file:
        template_contents = template_file.read()
    new_node = markdown_to_html_node(from_contents)
    title = extract_title(from_contents)
    template_contents = re.sub(r"{{ Title }}", title, template_contents)
    template_contents = re.sub(r"{{ Content }}", new_node, template_contents)
    directory_path = os.path.dirname(dest_path)
    os.makedirs(directory_path, exist_ok=True)
    with open(dest_path, mode="w") as dest_file:
        dest_file.write(template_contents)

def generate_pages_recursively(dir_path_content, template_path, dst):
    dir_path_list = os.listdir(dir_path_content)
    for item in dir_path_list:
        full_path = os.path.join(dir_path_content, item)
        html_file_type = re.sub(r"md", "html", item)
        dest_path = os.path.join(dst, html_file_type)
        if os.path.isfile(full_path):
            if item.endswith(".md"):
                generate_page(full_path, template_path, dest_path)
        elif os.path.isdir(full_path):
            generate_pages_recursively(full_path, template_path, dest_path)
