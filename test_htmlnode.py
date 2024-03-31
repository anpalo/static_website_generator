import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

children_test =  [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node1 = HTMLNode(tag="a", value="hello",children=None,props={"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node1.props_to_html(), 'class="greeting" href="https://boot.dev"')
     
    def test_props_to_html_false(self):
        props = {"href": "https://boot.dev"}
        node1 = HTMLNode(tag="a", value="hello",children=None,props=props)
        self.assertNotEqual(node1.props_to_html(), "")

    def test_to_html_leaf(self):
        node1 = LeafNode(tag="a", value="Click me!", props={"href": "https://boot.dev"})
        self.assertEqual(node1.to_html(), '<a href="https://boot.dev">Click me!</a>')
    


    def test_to_html_parent(self):
        node1 = ParentNode(tag="p", children=children_test)
        self.assertEqual(node1.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

        
    def test_to_html_self_closing_tag(self):
        node = LeafNode(tag="img", value=None, props={"src": "/path/to/image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="/path/to/image.jpg" alt="An image" />')



if __name__ == "__main__":
    unittest.main()
