import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_delimiter_list = []
    for node in old_nodes:
        if node.text_type == "text":
            split_text = node.text.split(delimiter)
            for i, part in enumerate(split_text):
                if i % 2 == 0:
                    new_delimiter_list.append(TextNode(part, text_type_text))
                else:
                    if i == len(split_text) - 1:
                        raise Exception("Unpaired delimiter symbol detected in text.")
                    else:
                        new_delimiter_list.append(TextNode(part, text_type))
        else:
            new_delimiter_list.append(node)
    return new_delimiter_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)   
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_node_list = []
    for node in old_nodes: 
        original_node_type = node.text_type
        images = extract_markdown_images(node.text)
        for image in images:
            image_markdown = f"![{image[0]}]({image[1]})"
            split_part = node.text.split(image_markdown)
            if split_part[0] != "":
                new_node_list.append(TextNode(split_part[0], original_node_type))
            new_image = TextNode(image[0], text_type_image, image[1])
            new_node_list.append(new_image)
            node.text = split_part[1]
        if node.text != "":
            new_node_list.append(TextNode(node.text, original_node_type))
    return new_node_list

def split_nodes_link(old_nodes):
    new_node_list = []
    for node in old_nodes:
        original_node_type = node.text_type
        links = extract_markdown_links(node.text)
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue 
        for link in links:
            link_markdown = f"[{link[0]}]({link[1]})"
            split_part = node.text.split(link_markdown)
            if split_part[0] != "":
                new_node_list.append(TextNode(split_part[0], original_node_type))
            new_link = TextNode(link[0], text_type_link, link[1])
            new_node_list.append(new_link)
            node.text = split_part[1]
        if node.text != "":
            new_node_list.append(TextNode(node.text, original_node_type))
    return new_node_list

def text_to_textnodes(text):
    nodes_list = [TextNode(text, text_type_text)]
    nodes_list = split_nodes_delimiter(nodes_list, "**", text_type_bold)
    nodes_list = split_nodes_delimiter(nodes_list, "*", text_type_italic)
    nodes_list = split_nodes_delimiter(nodes_list, "`", text_type_code)
    nodes_list = split_nodes_image(nodes_list)
    nodes_list = split_nodes_link(nodes_list)
    return nodes_list

