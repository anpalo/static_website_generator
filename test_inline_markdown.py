from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
import unittest

from textnode import (
    TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestInlineMarkdown(unittest.TestCase):

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" word", text_type_text),
])
    
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", text_type_text),
    TextNode("bold", text_type_bold),
    TextNode(" word", text_type_text),
])

    def test_double_bold(self):
            node = TextNode("This is **bold text** with **more bold words**.", text_type_text)
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            self.assertEqual(new_nodes, [
        TextNode("This is ", text_type_text),
        TextNode("bold text", text_type_bold),
        TextNode(" with ", text_type_text),
        TextNode("more bold words", text_type_bold),
        TextNode(".", text_type_text),
    ])

    def test_bold_2(self):
            node = TextNode("This is **bold text**.", text_type_text)
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            self.assertEqual(new_nodes, [
        TextNode("This is ", text_type_text),
        TextNode("bold text", text_type_bold),
        TextNode(".", text_type_text)
    ])
    
    def test_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        image_markdown = extract_markdown_images(text)
        self.assertEqual(image_markdown, [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])
        
    def test_markdown_links(self):
        text = "A link [bay](https://example.com/bay) and another [grove](https://example.com/grove)"
        link_markdown = extract_markdown_links(text)
        self.assertEqual(link_markdown, [("bay", "https://example.com/bay"), ("grove", "https://example.com/grove")])

    
    def test_split_nodes_image(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", 
                        text_type_text)        
        image_node_split = split_nodes_image([node])
        self.assertEqual(image_node_split, [
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
    ])


    def test_split_nodes_link(self):
         node = TextNode("This is text with a link [bay](https://example.com/bay) and another [grove](https://example.com/grove).", text_type_text)
         link_node_split = split_nodes_link([node])
         self.assertEqual(link_node_split, [
              TextNode("This is text with a link ", text_type_text),
              TextNode("bay", text_type_link, "https://example.com/bay"), 
              TextNode(" and another ", text_type_text), 
              TextNode("grove", text_type_link, "https://example.com/grove"),
              TextNode(".", text_type_text)
         ])

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)" 
        text_textnodes_return = text_to_textnodes(text)
        self.assertEqual(text_textnodes_return, [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev")
            ])
         
if __name__ == "__main__":
    unittest.main()