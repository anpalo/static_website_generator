import unittest
from block_markdown import markdown_to_blocks, block_to_block, markdown_to_html_node, extract_title
from block_markdown import(    
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list ,
    block_type_ordered_list,)





class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''
        new_markdown = markdown_to_blocks(text)
        self.assertEqual(new_markdown, [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ])


    def test_markdown_to_blocks_multiple_newlines(self):
        text = '''This is **bolded** paragraph





This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line




* This is a list
* with items
'''
        new_markdown = markdown_to_blocks(text)
        self.assertEqual(new_markdown, [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ])

    def test_block_to_block_heading(self):
        text_block = "# This is a **bolded** heading."
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_heading)
    
    def test_block_to_block_code(self):
        text_block = "```\nThis is a block of code\nwith multiple lines\nup to 3 lines\n```"
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_code)

    def test_block_to_block_quote(self):
        text_block = ">This is a quote block\nwith multiple lines\nup to 3 lines!"
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_quote)
    
    def test_block_to_block_ordered_list(self):
        text_block = "1. This is an ordered list\n2. with multiple lines\n3. up to 3 lines!"
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_ordered_list)
    
    def test_block_to_block_unordered_list(self):
        text_block = "* This is an unordered list\n- with multiple lines\n* up to 3 lines!"
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_unordered_list)
    
    def test_block_to_block_paragraph(self):
        text_block = "This is an paragraph block\nwith multiple lines\nup to 3 lines!"
        determine_block = block_to_block(text_block)
        self.assertEqual(determine_block, block_type_paragraph)
        

    def test_markdown_to_html(self):
        text = '''# This is a **header**

This is a paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''
        expected_html = "<div><h1>This is a <b>header</b></h1><p>This is a paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line</p><ul><li>This is a list</li><li>with items</li></ul></div>"
        actual_html = markdown_to_html_node(text)
        self.assertEqual(actual_html, expected_html)

 
if __name__ == "__main__":
    unittest.main()