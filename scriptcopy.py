import os
import shutil

def copy_to_subdirectories(src_file, dest_dir):
    """
    Copies a file to a directory and its subdirectories if the file doesn't already exist in those directories.

    :param src_file: The path to the source file to copy.
    :param dest_dir: The path to the destination directory.
    """
    for root, dirs, files in os.walk(dest_dir):
        if os.path.basename(src_file) in files:
            print(f"File '{src_file}' already exists in '{root}', skipping...")
        else:
            dest_file = os.path.join(root, os.path.basename(src_file))
            shutil.copy(src_file, dest_file)
            print(f"File '{src_file}' copied to '{dest_file}'.")


# Example usage:
src_file = "your/source/file/path"
dest_dir = "your/dest/dir"
copy_to_subdirectories(src_file, dest_dir)
