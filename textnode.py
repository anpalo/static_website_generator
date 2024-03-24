from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj_1):
        if self.text == obj_1.text and self.text_type == obj_1.text_type and self.url == obj_1.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"



def text_node_to_html_node(text_node):
    html_node = None
    if text_node.text_type == text_type_text:
        html_node = LeafNode(None,text_node.text)
    elif text_node.text_type == text_type_bold:
        html_node = LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        html_node = LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        html_node = LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        html_node = LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == text_type_image:
        html_node = LeafNode("img", "", {"src": text_node.url, "alt":text_node.text})
    else:
        raise ValueError(f"Invalid text type:'{text_node.text_type}'")
    return html_node
