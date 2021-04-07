import time
import psutil
while True:
    x = psutil.net_io_counters().bytes_recv
    x = x /1024./1024
    print(x)
    time.sleep(1)