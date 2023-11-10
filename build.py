#!/usr/bin/python

import os
import subprocess

def delete_dir_if_needed(top_dir):
    if(os.path.isdir(top_dir)):
        for root, dirs, files in os.walk(top_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(top_dir)

def update_version(dir):
    # Read in the file
    path = os.path.join(dir,'__init__.py')

    # Check is done before that this env variable exists
    new_version = os.getenv('VERSION', "")
    print(f"__version__ = \"{new_version}\"")

    # Write the file out again
    with open(path, 'w') as file:
        file.write(f"__version__ = \"{new_version}\"")

def generate_package(root_dir):
    cmd = "python3 -m build"
    subprocess.call(cmd, cwd=root_dir, shell=True)

def check_environement():
    # used by setup.py
    version = os.getenv('VERSION','')
    if(version == ''):
        raise Exception("missing env var VERSION")

    # used by publish_package function
    username = os.getenv('TWINE_USERNAME','')
    if(username == ''):
        raise Exception("missing env var TWINE_USERNAME")
    # reset username
    username = ''

    # used by publish_package function
    password = os.getenv('TWINE_PASSWORD','')
    if(password == ''):
        raise Exception("missing env var TWINE_PASSWORD")
    password = ''

def publish_package(root_dir):
    # used by publish_package function
    cmd = f"python3 -m twine upload dist/*"

    subprocess.call(cmd, cwd=root_dir, shell=True)


def main():
    # check env before doing anything
    check_environement()

    # define vars
    root = os.path.dirname(os.path.realpath(__file__))
    src_dir = os.path.join(root, "src")
    stx_dir = os.path.join(src_dir, "systemathics","apis")
    dist_dir = os.path.join(src_dir, "dist")

    print("Clean old generated code")
    delete_dir_if_needed(dist_dir)

    # generate package
    print("Setting version in setup.py")
    update_version(stx_dir)
    print("Generate package")
    generate_package(src_dir)
    
    # publish package
    print("Publish package")
    publish_package(src_dir)

if __name__ == "__main__":
    # execute only if run as a script
    main()
