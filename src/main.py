import os
import sys
import shutil
from generator import generate_pages_recursive

def copy_contents():
    src_dir = os.path.join(os.path.dirname(__file__), "../static")
    dst_dir = os.path.join(os.path.dirname(__file__), "../docs")
   ##delete all files and folders in the destination directory and log the deletes
    for filename in os.listdir(dst_dir):
        file_path = os.path.join(dst_dir, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            print(f"Deleted file: {file_path}")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Deleted directory: {file_path}")

    #copy all files and folders from the source directory to the destination directory and log each copy
    for filename in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, filename)
        dst_file_path = os.path.join(dst_dir, filename)
        if os.path.isfile(src_file_path):
            shutil.copy2(src_file_path, dst_file_path)
            print(f"Copied file: {src_file_path} to {dst_file_path}")
        elif os.path.isdir(src_file_path):
            shutil.copytree(src_file_path, dst_file_path)
            print(f"Copied directory: {src_file_path} to {dst_file_path}")



def main():
    #grab basepath from first argument. If none provided, use none. Log the basepath being used.
    basepath = sys.argv[1] if len(sys.argv) > 1 else ""
    print(f"#####Running static site builder from {basepath}")
    copy_contents()
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()