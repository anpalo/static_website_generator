import os
import shutil

def copy_directory(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for item in os.listdir(path=src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        print(f" * {src_path} -> {dst_path}")

        if os.path.isdir(src_path):
            copy_directory(src_path, dst_path)
        else:
            shutil.copy(src=src_path, dst=dst_path)

