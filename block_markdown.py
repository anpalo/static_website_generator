from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(text):
    stripped_text = []
    split_text = text.split("\n\n")
    for line in split_text:
        line = line.strip()
        if line != "":
            stripped_text.append(line)       
    return stripped_text


def block_to_block(text_block):
    lines = text_block.split("\n")
    if len(lines) > 1:
        if lines[0].startswith("```") and lines[-1].startswith("```"):
            return block_type_code
    for i, line in enumerate(lines):
        if line.startswith("#"):
            count = 0
            for char in line:
                if char == "#":
                    count += 1
                else:
                    break
            if 1 <= count <= 6:
                if len(line) > count and line[count] == " ":
                    return block_type_heading     
        elif line[0] == ">":
            return block_type_quote
        elif line.startswith("* ") or line.startswith("- "):
            for ln in lines[1:]:
                if not (ln.startswith("* ") or ln.startswith("- ")):
                    return block_type_paragraph
            return block_type_unordered_list

    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            return block_type_paragraph
    else:
        return block_type_ordered_list
    return block_type_paragraph

def text_to_child(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_child = text_node_to_html_node(node)
        children.append(html_child)
    return children

def code_block_to_html(code_block):
    split_block = code_block.split("\n")
    remove_first_last = split_block[1:-1]
    code_block_text = "\n".join(remove_first_last)
    child_text = text_to_child(code_block_text)
    code_node = ParentNode(tag="code", children=child_text)
    code_node_parent = ParentNode(tag="pre", children=[code_node])
    return code_node_parent

def quote_block_to_html(quote_block):
    removed_quote_marker = re.sub(r"(^>)", '', quote_block, flags=re.MULTILINE)  # use ^ to inspect the first character of each new line. ^> to match any > at the start of the line
    child_text = text_to_child(removed_quote_marker.strip())
    quote_node = ParentNode(tag="blockquote", children=child_text) # strip the whitespace that comes after > in quote markdown
    return quote_node

def unordered_list_to_html(ul_text):
    li_nodes = []
    removed_ul_marker = re.sub(r"^(?:\*|-) ", '', ul_text, flags=re.MULTILINE)
    split_ul_lines = removed_ul_marker.split("\n")
    for line in split_ul_lines:
        child_text = text_to_child(line)
        new_node = ParentNode(tag="li", children=child_text)
        li_nodes.append(new_node)
    ul_node_parent = ParentNode(tag="ul", children=li_nodes)
    return ul_node_parent

def ordered_list_to_html(ol_text):
    li_nodes = []
    removed_ol_marker = re.sub(r"^(?:\d+\.) ", '', ol_text, flags=re.MULTILINE)  # use \d+ to capture digits of any size
    split_ol_lines = removed_ol_marker.split("\n")
    for line in split_ol_lines:
        child_text = text_to_child(line)
        new_node = ParentNode(tag="li", children=child_text)
        li_nodes.append(new_node)
    ol_node_parent = ParentNode(tag="ol", children=li_nodes)
    return ol_node_parent

def header_to_html(header_text):
    match = re.match(r"^(#{1,6}) (.*)", header_text) # find initial #s in range 1-6. Add space. Greedy match the remaining text.
    if match:
        level = len(match.group(1)) # store the matched #s
        text = match.group(2)  # get the text without the #s
        child_text = text_to_child(text)
        header_node = ParentNode(tag=f"h{level}", children=child_text)
        return header_node
    else:
        return None
def paragraph_to_html(paragraph_block):
    lines = paragraph_block.split("\n")
    paragraph = " ".join(lines)
    child_text = text_to_child(paragraph)
    paragraph_node = ParentNode(tag="p", children=child_text)
    return paragraph_node


def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown) # separate text into blocks (based on whitespace separation)
    for block_text in blocks: # go through each block and check its type. Depending on the type, create a node of that type to be stored and later wrapped in the div
        type = block_to_block(block_text)
        if type == block_type_code:
           code_node = code_block_to_html(block_text)
           html_nodes.append(code_node)
        elif type == block_type_quote:
            quote_node = quote_block_to_html(block_text)
            html_nodes.append(quote_node)
        elif type == block_type_heading:
            header_node = header_to_html(block_text)
            html_nodes.append(header_node)
        elif type == block_type_unordered_list:
            ul_node = unordered_list_to_html(block_text)
            html_nodes.append(ul_node)
        elif type == block_type_ordered_list:
            ol_node = ordered_list_to_html(block_text)
            html_nodes.append(ol_node)
        else:
            paragraph_node = paragraph_to_html(block_text)
            html_nodes.append(paragraph_node)
    div_node = ParentNode(tag="div", children=html_nodes) # wrap a div tag around the other stored nodes
    return div_node.to_html()


           
           
