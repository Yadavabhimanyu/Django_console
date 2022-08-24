import os
##
##os.system('python D:\Vendors\product\Basics\hello.py')

from subprocess import run
import sys

function_li=["D:\Vendors\product\hello.py","D:\Vendors\product\main.py","D:\Vendors\product\hello.py"]
def external(function_li):
    for i in function_li:
        out= run([sys.executable,i],capture_output=True, text=True)
        print("stdout",out.stdout)
        print("stderr",out.stderr,len(out.stderr))
        if out.stderr == '':
            print("no error")
        else:
            raise Exception(out.stderr)
        

external(function_li)

