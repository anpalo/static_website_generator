from copy_static import copy_directory
from generate_page import generate_pages_recursively
import os
import shutil

# Make sure the paths are correct based on your project structure and naming system
static_path = "src/static"
public_path = "src/public"
from_path = "src/content"  
template_path = "src/template.html"  
dest_path = "src/public"  # This is the target file path

def main():

    shutil.rmtree(public_path, ignore_errors=True)
    os.makedirs(public_path, exist_ok=True)
    copy_directory(static_path, public_path)
   

    generate_pages_recursively(from_path,template_path,dest_path)
   
if __name__ == "__main__":         
    main()

print("Content generation completed, index.html and other content should now exist in the 'public' directory.")
