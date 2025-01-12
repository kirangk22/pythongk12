import time
time_sec=3602


#for i in reversed(range(0,time_sec)):
for i in range(time_sec,0,-1):
    sec=i%60
    min=int((i/60))%60
    hour=int((i/3600))    # in hour 3600 secons
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)


