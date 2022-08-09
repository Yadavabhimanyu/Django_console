from django.shortcuts import render
from subprocess import run
import sys
import os
from .functions.functions import handle_uploaded_file
from .models import process_file_repo


##########Custom functions###
def external(function_li, process_name):
    for i in function_li:
        path = os.getcwd()
        folder_path = r"avionics_app/static/upload"
        path_f = os.path.join(path, folder_path)
        print(i, "iiiiiiiiiiiii")
        process_folder = os.path.join(path_f, process_name)
        j = os.path.join(process_folder, i)
        out = run([sys.executable, j], capture_output=True, text=True)
        print("stdout", out.stdout)
        print("stderr", out.stderr, len(out.stderr))
        if out.stderr == '':
            print("no error")
        else:
            raise Exception(out.stderr)


#####################
# Create your views here.
def index(request):
    context = {"status": 'status at index page'}
    return render(request, 'index.html', context)

def convert_to_24_h(hour):
    if "AM" in hour:
        if "12" in hour[:2]:
            return "00" + hour[2:-2]
        return hour[:-2]
    elif "PM" in hour:
        if "12" in hour[:2]:
            return hour[:-2]
    return str(int(hour[:2]) + 12) + hour[2:5]

def new_process(request):
    if request.method == 'POST':
        print("ggggggggggggggggggg")
        project_name=request.POST.get('projectName')
        process_name=request.POST.get('processName')
        from_date=request.POST.get('fromdate')
        to_date=request.POST.get('todate')
        to_time=str(request.POST.get('totime'))
        print(to_time)
        if len(to_time.split(':')[0])==1:
            to_time='0'+to_time
        to_time=convert_to_24_h(to_time)
        print(to_time)
        project_file=''
        for i in request.FILES.keys():
            project_f = request.FILES[i].name
            if project_file=='':
                project_file=project_file+project_f
            else:
                project_file=project_file+','+project_f
            handle_uploaded_file(request.FILES[i], request.POST.get('projectName'))
            # external([project_f], request.POST.get('projectName'))
        data_li = process_file_repo(project_name=project_name,process_name=process_name,from_date=from_date,to_date=to_date,to_time=to_time,project_file=project_file)
        data_li.save()
    projects=process_file_repo.objects.all()
    context = {"projects":  projects}

    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html')

def schedule_project(request,pk):
    process = process_file_repo.objects.filter(project_name=pk)
    project_file_li=[]
    for proc in process:
        project_file=proc.project_file.split(',')
        project_file_li.append(project_file)
    context={'process':project_file_li}
    return render(request,'schedule_project.html',context)