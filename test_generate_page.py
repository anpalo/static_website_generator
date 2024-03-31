import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):


    def test_extract_title(self):
        text = text = '''# This is a header

This is a paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''
        expected_text = "This is a header"
        actual_text = extract_title(text)
        self.assertEqual(expected_text, actual_text)
    
    def test_extract_title_no_header(self):
        text = text = '''## This is a header

This is a paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
'''
        with self.assertRaises(Exception):
            extract_title(text)
   

if __name__ == "__main__":
    unittest.main()