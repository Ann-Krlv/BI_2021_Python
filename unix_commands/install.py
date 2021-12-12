#!/usr/bin/env python3
import os
import shutil
import stat


dest_folder = os.environ['PATH'].split(os.pathsep)[0]
utils_list = ['ls.py', 'rm.py', 'sort.py', 'wc.py']
for i in utils_list:
    dest = os.path.join(dest_folder, i)
    source = os.path.abspath(i)
    new_path = shutil.copyfile(source, dest)
    os.chmod(new_path, stat.S_IRWXU)


