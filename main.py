import subprocess
import os
import sys
import time
from pathlib import Path
import codecs
path = r'C:\htzqzyb2'
git = r'C:\htzqzyb2\.git'
if os.path.exists(path):
    child = subprocess.Popen(r'C:\htzqzyb2\hexin.exe',shell=True)
    child.wait()
    if os.path.exists(git):
        cd = subprocess.Popen(r'cd C:\htzqzyb2',shell=True)
        cd.wait()
    init = subprocess.Popen(r'git init',shell=True)
    init.wait()
    remote = subprocess.Popen(r'git remote add origin https://github.com/Mryan2005/MyFather-sOs.git',shell=True)
    remote.wait()
    add = subprocess.Popen(r'git add .',shell=True)
    add.wait()
    commit = subprocess.Popen('git commit -m update',shell=True)
    commit.wait()
    push = subprocess.Popen('git push origin',shell=True)
    push.wait()
else:
    child = subprocess.Popen(r'cd C:\ ')  
    child = subprocess.Popen('git clone https://github.com/Mryan2005/MyFather-sOs.git')
