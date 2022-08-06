import os
def handle_uploaded_file(f,process_name):
    path = os.getcwd()
    folder_path = f"avionics_app/static/upload"
    path_f = os.path.join(path, folder_path)
    process_folder=os.path.join(path_f,process_name)
    if os.path.exists(process_folder):
        print('jjjjj')
    else:
        os.makedirs(process_folder)

    with open('avionics_app/static/upload/'+process_name+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)