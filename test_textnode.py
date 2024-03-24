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


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", 89)
        self.assertNotEqual(node, node2)
    
    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", None)
        self.assertNotEqual(node, node2)
    
    def test_eq_false3(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
    
    def test_eq_false4(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node????", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_url_false(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )
   


if __name__ == "__main__":
    unittest.main()
