# Schedule Library imported
import schedule
import time
from datetime import datetime
import os
from .models import process_file_repo



#############
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
# Functions setup

projects= process_file_repo.objects.order_by().values_list('project_name').distinct()
print(projects)
def sudo_placement():
	print("Get ready for Sudo Placement at Geeksforgeeks")


schedule.every().day.at("11:05").do(sudo_placement)
#
# while True:
#
# 	# Checks whether a scheduled task
# 	# is pending to run or not
# 	print(datetime.now())
# 	schedule.run_pending()
# 	time.sleep(1)
