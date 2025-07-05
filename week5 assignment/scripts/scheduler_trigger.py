import schedule
import time
from scripts.export_data import export_table

def job():
    print("Running scheduled export...")
    for table in ['users', 'orders']:
        export_table(table)

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
