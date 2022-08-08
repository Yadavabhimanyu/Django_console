from django.shortcuts import render
from subprocess import run
import sys
import os
from .functions.functions import handle_uploaded_file


##########Custom functions###
def external(function_li,process_name):
    for i in function_li:
        path=os.getcwd()
        folder_path = r"avionics_app/static/upload"
        path_f=os.path.join(path,folder_path)
        print(i,"iiiiiiiiiiiii")
        process_folder = os.path.join(path_f, process_name)
        j=os.path.join(process_folder,i)
        out= run([sys.executable,j],capture_output=True, text=True)
        print("stdout",out.stdout)
        print("stderr",out.stderr,len(out.stderr))
        if out.stderr == '':
            print("no error")
        else:
            raise Exception(out.stderr)

#####################
# Create your views here.
def index(request):
    context={"status":'status at index page'}
    return render(request,'index.html',context)

def new_process(request):
    if request.method=='POST':
        print("ggggggggggggggggggg")
        print(request.POST.get('projectName'))
        print(request.POST.get('processName'))
        print(request.POST.get('fromdate'),"frommmdate")
        print(request.POST.get('todate'),"tooodate")
        print(request.POST.get('totime'),"totimeeeeeeeeee")
        for i in request.FILES.keys():
            handle_uploaded_file(request.FILES[i],request.POST.get('projectName'))
            project_f = request.FILES[i].name
            external([project_f],request.POST.get('projectName'))
    context = {"status":request.POST.get('projectName')}

    return render(request,'index.html',context)

def login(request):
    context={}
    return render(request,'login.html')