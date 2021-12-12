#!/usr/bin/env python3
import os
import shutil
import stat


dest_folder = os.environ['PATH'].split(os.pathsep)[0]
sys.stdout.write(f'The destination folder in PATH is {dest_folder}')
utils_list = ['ls.py', 'rm.py', 'sort.py', 'wc.py', 'grep.py', 'cat.py', 'tail.py', 'mkdir.py']

for i in utils_list:
    dest = os.path.join(dest_folder, i)
    source = os.path.abspath(i)
    os.chmod(source, stat.S_IRWXU)
    new_path = shutil.copyfile(source, dest)
    sys.stdout.write(f'The {source} has copied to {new_path}')
    os.chmod(new_path, stat.S_IRWXU)
