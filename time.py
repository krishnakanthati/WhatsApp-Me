from apscheduler.schedulers.blocking import BlockingScheduler
from automate import send

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send, 'interval', minutes=15)

sched.start()
