import os
from django.conf import settings
value = settings.BASE_DIR

def handle_uploaded_file(f,process_name):
    print(process_name)
    path= value
    folder_path = f"avionics_app/static/upload"
    path_f = os.path.join(path, folder_path)
    process_folder=os.path.join(path_f,process_name)
    print(process_folder)
    print(f,"lengthhhhhhhh")
    if os.path.exists(process_folder):
        print('jjjjj')
    else:
        os.makedirs(process_folder)

    with open('avionics_app/static/upload/'+process_name+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def convert_to_24_h(hour):
    if "AM" in hour or 'a.m.' in hour:
        if "12" in hour[:2]:
            return "00" + hour[2:-2]
        return hour[:-2]
    elif "PM" in hour or 'p.m.' in hour:
        if "12" in hour[:2]:
            return hour[:-2]
    return str(int(hour[:2]) + 12) + hour[2:5]


def clear_old_files(process_name):
    path = value
    folder_path = f"avionics_app/static/upload"
    path_f = os.path.join(path, folder_path)
    process_folder = os.path.join(path_f, process_name)
    print(process_folder,"proces folder")
    if os.path.exists(process_folder):
        print('jjjjj')
        for j in os.listdir(process_folder):
            os.remove(os.path.join(process_folder, j))

