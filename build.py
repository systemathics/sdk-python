import os
import subprocess

def create_dir_if_needed(dir):
    if(not(os.path.isdir(dir))):
        os.makedirs(dir)

def delete_dir_if_needed(top_dir):
    if(os.path.isdir(top_dir)):
        for root, dirs, files in os.walk(top_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(top_dir)

def is_grpc_file (path):
    """Test if a *.proto file describe a grpc service"""
    for line in open(path, 'r').readlines() :
        if line.startswith('service ') :
            return True
    return False

def sort_proto_files(dir):
    """Used to sort *.proto files under a directory `dir` in 2 categories :
    - grpc files (containing a a grpc service)
    - proto files (without a a grpc service)

    Returns a tuple with 2 lists. 
    First list containts grpc files. 
    Second list containt regular proto files
    """
    grpc_files = []
    proto_files = []
    for root, dirs, files in os.walk(dir, topdown=True):
        # skip google folder
        if 'google' in dirs:
            dirs.remove('google')
        for file in files:
            path = os.path.join(root, file)
            if (file.endswith('.proto')) :
                if(is_grpc_file(path)) :
                    grpc_files.append(path)
                else:
                    proto_files.append(path)
    return (grpc_files,proto_files)

def generate_grpc_file(files, scr_dir, target_dir):
    create_dir_if_needed(target_dir)
    all_files= " ".join(files)
    cmd = f"python3 -m grpc_tools.protoc --proto_path={scr_dir} --python_out={target_dir} --grpc_python_out={target_dir} {all_files}"
    print(cmd)
    subprocess.call(cmd, cwd=scr_dir, shell=True)

def generate_proto_file(files, scr_dir, target_dir):
    all_files= " ".join(files)
    create_dir_if_needed(target_dir)
    cmd = f"python3 -m grpc_tools.protoc --proto_path={scr_dir} --python_out={target_dir} {all_files}"
    print(cmd)
    subprocess.call(cmd, cwd=scr_dir, shell=True)

def generate(tuple_of_list, src_dir, target_dir):
    grpc_files = tuple_of_list[0]
    proto_files = tuple_of_list[1]

    generate_grpc_file(grpc_files, src_dir, target_dir)
    generate_proto_file(proto_files, src_dir, target_dir)

def add_namespace_import_to_init_py(dir):
    for root, _, _ in os.walk(dir, topdown=True):
        path = os.path.join(root,'__init__.py')
        with open(path, 'w') as f:
            f.write("__import__('pkg_resources').declare_namespace(__name__)")

def extract_version(data):
    version_pattern ='version="'
    l = len(version_pattern)
    start = data.find('version="')
    end = data.find('"', start + l + 1)
    return data[start + l : end]

def replace_version_in_setup(dir):
    # Read in the file
    path = os.path.join(dir,'setup.py')
    with open(path, 'r') as file :
        filedata = file.read()

    old_version = extract_version(filedata)

    # Check is done before taht this env variable exists
    new_version = os.getenv('VERSION', "")

    # Replace the target string
    filedata = filedata.replace(old_version, new_version)

    # Write the file out again
    with open(path, 'w') as file:
        file.write(filedata)

def generate_package(root_dir):
    cmd = "python3 setup.py sdist"
    subprocess.call(cmd, cwd=root_dir, shell=True)

def check_environement():
    # used by setup.py
    version = os.getenv('VERSION','')
    if(version == ''):
        raise Exception("missing env var VERSION")

    # used by publish_package function
    key = os.getenv('PYPI_PUBLISH_INDIRECT_KEY','')
    if(key == ''):
        raise Exception("missing env var PYPI_PUBLISH_INDIRECT_KEY")

    # used by publish_package function
    user = os.getenv('PYPI_USERNAME','')
    if(user == ''):
        raise Exception("missing env var PYPI_USERNAME")

    # used by publish_package function
    repository = os.getenv('PYPI_REPOSITORY','')
    if(repository == ''):
        raise Exception("missing env var PYPI_REPOSITORY")

def publish_test_package(root_dir):
    # pass_out generated with
    # > echo -n ${{PASSWORD}} > ./pass
    # > openssl aes-256-cbc -pbkdf2 -e -k "${{PYPI_PUBLISH_INDIRECT_KEY}}" < ./pass > ./pass_out

    # used by publish_package function
    key = os.getenv('PYPI_PUBLISH_INDIRECT_KEY','')
    if(key == ''):
        raise Exception("missing env var PYPI_PUBLISH_INDIRECT_KEY")

    # used by publish_package function
    user = os.getenv('PYPI_USERNAME','')
    if(user == ''):
        raise Exception("missing env var PYPI_USERNAME")

    # used by publish_package function
    repository = os.getenv('PYPI_REPOSITORY','')
    if(repository == ''):
        raise Exception("missing env var PYPI_REPOSITORY")

    # convert password, as strange chars are not always accepted in env var...
    path = os.path.join(root_dir, "pass")
    path_out = os.path.join(root_dir, "..", "pass_out")
    openssl_cmd = f'openssl aes-256-cbc -pbkdf2 -d -k "{key}" < {path_out} > {path}'
    subprocess.call(openssl_cmd, cwd=root_dir, shell=True)

    with open(path, 'r') as f:
        password = f.read()

    cmd = f"python3 -m twine upload --repository {repository} dist/* -u {user} -p '{password}'"

    os.remove(path)
    subprocess.call(cmd, cwd=root_dir, shell=True)

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
    out_dir = os.path.join(root, "python")
    stx_dir = os.path.join(out_dir, "systemathics")
    dist_dir = os.path.join(out_dir, "dist")

    print("Clean old generated code")
    create_dir_if_needed(out_dir)
    delete_dir_if_needed(stx_dir)
    delete_dir_if_needed(dist_dir)

    # get proto files (grpc and regular)
    print("Sort proto files")
    result = sort_proto_files(src_dir)
    # generate new python file from proto
    print("Generate proto files")
    generate(result, src_dir, out_dir)

    # add proto import to __init__.py files
    print("Add namespace import to __init__.py files")
    add_namespace_import_to_init_py(stx_dir)

    # geenrate and publish package
    print("Setting version in setup.py")
    replace_version_in_setup(out_dir)
    print("Generate package")
    generate_package(out_dir)
    print("Publish package")
    publish_package(out_dir)



if __name__ == "__main__":
    # execute only if run as a script
    main()

