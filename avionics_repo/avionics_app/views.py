from django.shortcuts import render,redirect
from django.http import HttpResponse
from subprocess import run
import sys
import os
from .models import process_file_repo
from .functions.functions import handle_uploaded_file,convert_to_24_h,clear_old_files


#####################
# Create your views here.
def index(request):
    print(os.system('which python'))
    projects = process_file_repo.objects.all()
    context = {"projects": projects}
    return render(request, 'index.html', context)


def new_process(request):
    if request.method == 'POST':
        try:
            project_name=request.POST.get('projectName')
            process_name=request.POST.get('processName')
            from_date=request.POST.get('fromdate')
            to_date=request.POST.get('todate')
            to_time=str(request.POST.get('totime'))
            if len(to_time.split(':')[0])==1:
                to_time='0'+to_time
            to_time=convert_to_24_h(to_time)
            project_file=''
            for i in request.FILES.keys():
                project_f = request.FILES[i].name
                if project_file=='':
                    project_file=project_file+project_f
                else:
                    project_file=project_file+','+project_f
                handle_uploaded_file(request.FILES[i], project_name +'/'+ process_name )
            data_li = process_file_repo(project_name=project_name,process_name=process_name,from_date=from_date,to_date=to_date,to_time=to_time,project_file=project_file)
            data_li.save()
        except Exception as e:
            print(e)
            if "already exists" in str(e):
                projects = process_file_repo.objects.all()
                context={'process_check':'alreadyexists',"projects":  projects}
                return render(request,'index.html',context)
            else:
                projects = process_file_repo.objects.all()
                context = {'process_check': 'error',"projects":  projects}
                return render(request, 'index.html', context)
    projects=process_file_repo.objects.all()
    context = {"projects":  projects}
    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html')

def schedule_project(request,pk):
    if request.method=='POST':
        data_li=list(request.POST.values())
        data_str=''
        for data in data_li[1:]:
            if data_str=='':
                data_str=data
            else:
                data_str=data_str+','+data
        affected_surveys = process_file_repo.objects.filter(process_name=pk).update(project_file=data_str)
        print(affected_surveys,"affected_surveys")
        return redirect('index')
    process = process_file_repo.objects.filter(process_name=pk)
    print(process)
    project_file_li=[]
    for proc in process:
        project_file=proc.project_file.split(',')
        project_file_li.append(project_file)
    context={'process':project_file_li,'pk':pk}
    return render(request,'schedule_project.html',context)


def delete_process(request,pk):
    process = process_file_repo.objects.get(id=pk)
    if request.method == 'POST':
        process.delete()
        return redirect('index')
    return render(request,'delete_page.html',{'obj':process})


def update_task(request,pk):
    process = process_file_repo.objects.get(id=pk)
    if request.method == 'POST':
        project_name = request.POST.get('projectName')
        process_name = request.POST.get('processName')
        from_date = request.POST.get('fromdate')
        to_date = request.POST.get('todate')
        to_time = str(request.POST.get('totime'))
        print(to_time)
        if ':' in to_time:
            if len(to_time.split(':')[0]) == 1:
                to_time = '0' + to_time
        else:
            to_time=to_time.split(' ')[0]+':00 '+ to_time.split(' ')[1].replace('.','').upper()
        to_time = convert_to_24_h(to_time)
        print(to_time)
        project_file = ''
        if len(list(request.FILES.keys()))!=0:
            clear_old_files(project_name + '/' + process_name)
        for i in request.FILES.keys():
            project_f = request.FILES[i].name
            if project_file == '':
                project_file = project_file + project_f
            else:
                project_file = project_file + ',' + project_f
            handle_uploaded_file(request.FILES[i], project_name + '/' + process_name)
        process.project_name=project_name
        process.process_name=process_name
        process.from_date=from_date
        process.to_date=to_date
        process.to_time=to_time
        if len(project_file)!=0:
            process.project_file=project_file


        process.save()
        return redirect('index')
    context={'obj': process}
    return render(request,'update_task.html',context)

