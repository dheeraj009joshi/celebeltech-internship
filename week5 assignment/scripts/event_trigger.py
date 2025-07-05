from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scripts.export_data import export_table
import time

class TriggerHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".trigger"):
            print("Trigger file detected!")
            for table in ['users', 'orders']:
                export_table(table)

observer = Observer()
observer.schedule(TriggerHandler(), path=".", recursive=False)
observer.start()
print("Watching for trigger files...")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
