from textnode import (
    TextNode, 
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

print("\n\nmain.py working...\n\n")

def main():
    tn = TextNode("a", text_type_bold, "https://www.boot.dev")
    print(f"{tn}\n\n\n")

         
    


main()