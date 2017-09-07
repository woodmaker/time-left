import time

def print_time(hour, minute, second):
    print("{:0>2d}:{:0>2d}:{:0>2d}".format(hour, minute, second), 
            end="\r")

while(True):
    now = time.localtime()

    hour_now = now.tm_hour
    min_now = now.tm_min
    sec_now = now.tm_sec

    hour_rem = 0
    for shift_end in [6, 14, 22, 30]:
        if(hour_now<shift_end or hour_now==shift_end and min_now<15):
            hour_rem = shift_end-hour_now
            break

    sec_rem = (60-sec_now)%60
    min_rem = 14-min_now
    if sec_rem==0:
        min_rem = min_rem+1
    if min_rem<0:
        hour_rem = hour_rem-1
        min_rem = min_rem+60

    print_time(hour_rem, min_rem, sec_rem)
    time.sleep(1)
