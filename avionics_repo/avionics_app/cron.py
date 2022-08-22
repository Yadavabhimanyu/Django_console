# Schedule Library imported
import cronjobs
import schedule
from time import sleep
from datetime import *
import os
import psycopg2
from subprocess import run
import sys
import threading

conn = psycopg2.connect(database="Product_demo", user='postgres', password='albert123', host='localhost', port='5432')
cursor = conn.cursor()


###############
def external(function_li, process_name, project_name):
    print("thread started")
    for i in function_li:
        path = os.getcwd()
        folder_path = r"avionics_app/static/upload"
        ##        path_f = os.path.join(path, folder_path)
        ##        print(i, "iiiiiiiiiiiii")
        path_f = r"D:\Vendors\product\console_repo\Avionics_Repo\avionics_repo\avionics_app\static\upload"
        process_path = project_name + '/' + process_name
        process_folder = os.path.join(path_f, process_path)
        j = os.path.join(process_folder, i)
        out = run([sys.executable, j], capture_output=True, text=True)
        print("stdout", out.stdout)
        print("stderr", out.stderr, len(out.stderr))
        if out.stderr == '':
            print("no error")
        else:
            raise Exception(out.stderr)


###########

@cronjobs.register
def cron_func():
    querry = "select distinct process_name from process_file_repo"
    cursor.execute(querry)
    data = cursor.fetchall()

    project_li = []
    for d in data:
        project_li.append(d[0])

    for project in project_li:
        print(project)
        proj_querry = f"select * from process_file_repo where process_name ='{project}'"
        cursor.execute(proj_querry)
        project_data_tuple = cursor.fetchall()
        project_data_li = []
        for pro in project_data_tuple:
            project_data_li.append(list(pro))

        current_date = date.today()
        current_time = datetime.now().strftime('%H:%M:%S')
        print(current_date, project_data_li[0][2], project_data_li[0][3])

        if current_date >= project_data_li[0][2] and current_date <= project_data_li[0][3]:
            if current_time == str(project_data_li[0][4]):
                print("priiii")
                t1 = threading.Thread(target=external,
                                      args=(project_data_li[0][5].split(','), project, project_data_li[0][6]))
                t1.start()
            else:
                print("process time not yet ")
        else:
            print("process date expired")

    #############

