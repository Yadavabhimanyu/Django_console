from apscheduler.schedulers.background import BackgroundScheduler
import time
import tzlocal
import logging

##logging.basicConfig()
##logging.getLogger('apscheduler').setLevel(logging.DEBUG)
print(str(tzlocal.get_localzone()))

def test_job(num):
    for i in range(num):
        print(i,"hello")
##    time.sleep(5)
        
scheduler=BackgroundScheduler(timezone=str(tzlocal.get_localzone()))

##scheduler.add_job(test_job,'interval',seconds=5,id='my_job_id_1')

##scheduler.add_job(test_job, 'cron', hour=12, minute=48)
for j in range(4):
    scheduler.add_job(test_job, 'cron', name='func1',args=[j+10],day_of_week='*', hour=15, minute=22, end_date='2022-09-08',id='my_job_id_1'+str(j),replace_existing=True)
scheduler.start()
scheduler.print_jobs()
print(scheduler.get_jobs())
    

