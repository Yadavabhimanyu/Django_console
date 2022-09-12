from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import external
import tzlocal
from avionics_app.models import process_file_repo


def start():
    global all_jobs
    scheduler=BackgroundScheduler(timezone=str(tzlocal.get_localzone()))
    all_process=process_file_repo.objects.all()
    scheduler.start()
    for proc in all_process:
        project_name_=proc.project_name
        process_name_=proc.process_name
        project_file_=proc.project_file
        to_time_=str(proc.to_time)
        hour_=to_time_.split(':')[0]
        minutes_ = to_time_.split(':')[1]
        print("ypppppppppp")
        scheduler.add_job(external, 'cron', args=[project_file_.split(','),process_name_,project_name_], day_of_week='*', hour=hour_,
                          minute=minutes_, id=project_name_+'_'+process_name_,replace_existing=True,name=process_name_)
    scheduler.print_jobs()
    all_jobs=scheduler.get_jobs()
    print(all_jobs)

