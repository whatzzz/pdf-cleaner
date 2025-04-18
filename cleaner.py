import os
import threading
import time

def start_cleanup_timer(upload_folder, interval_minutes=5):
    def cleanup_loop():
        while True:
            now = time.time()
            for filename in os.listdir(upload_folder):
                filepath = os.path.join(upload_folder, filename)
                if os.path.isfile(filepath):
                    if now - os.path.getmtime(filepath) > interval_minutes * 60:
                        os.remove(filepath)
            time.sleep(60)

    t = threading.Thread(target=cleanup_loop, daemon=True)
    t.start()
