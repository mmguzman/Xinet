__author__ = 'silvia valencia'

import os
from os import walk, path, getcwd
from os.path import join
from shutil import copyfile, copystat, rmtree
from robot.libdoc import libdoc

CURRENT_DIRECTORY = getcwd()
DOCUMENTATION_DIRECTORY = "documentation"
RESOURCES_DIRECTORY = "resources"
PAGES_DIRECTORY = "pages"
FORMAT_EXTENSION = ".html"


def copy_dir(src, dst, follow_sym=True):
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    if os.path.isdir(src):
        copyfile(src, dst, follow_symlinks=follow_sym)
        copystat(src, dst, follow_symlinks=follow_sym)
    return dst


def copy_directory_tree(src, dst, symlinks=False, ignore=None):
    """Recursively copy a directory tree using copy_dir()."""
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copy_directory_tree(srcname, dstname, symlinks, ignore)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy_dir(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except EnvironmentError, why:
            errors.append((srcname, dstname, str(why)))
    try:
        copystat(src, dst)
    except OSError, why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.append((src, dst, str(why)))
    if errors:
        raise errors


def create_documentation_directory():
    # Create the documentation directory, if already exist it is removed and recreated."""
    source_dir = join(CURRENT_DIRECTORY, RESOURCES_DIRECTORY)
    destination_dir = join(CURRENT_DIRECTORY, DOCUMENTATION_DIRECTORY)

    if path.exists(destination_dir):
        rmtree(destination_dir)
    if not path.exists(destination_dir):
        copy_directory_tree(source_dir, destination_dir)


def get_filepaths(directory):
    """Gets the file names in a directory tree by walking the tree either top-down or bottom-up.
    For each directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in walk(directory):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("_"):
                # Join the two strings in order to form the full filepath.
                file_path = join(root, filename)
                file_paths.append(file_path)
    return file_paths


def make_file_documentation(source_file_path):
    """Generates the documentation for the file specified in the ``source_file_path`` argument."""
    file_name = source_file_path.replace(RESOURCES_DIRECTORY, DOCUMENTATION_DIRECTORY)
    file_name = file_name.rsplit('.', 1)[0]
    doc_file = file_name + FORMAT_EXTENSION
    libdoc(source_file_path, doc_file)


def generate_keyword_documentation():
    """Generates the documentation for all the .py resources."""
    # Create the documentation directory tree
    create_documentation_directory()

    # Get the list of py resources (full paths)
    full_file_paths = get_filepaths(join(CURRENT_DIRECTORY, RESOURCES_DIRECTORY))

    # Make the documentation for all the py resource files
    for filename in full_file_paths:
        make_file_documentation(filename)


generate_keyword_documentation()