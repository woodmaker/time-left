import time

while(True):
    a = time.asctime()

    hours = int(a[11:13])
    minutes = int(a[14:16])
    seconds = int(a[17:19])

    hr, mr = 0, 0
    if(hours<6 or hours==6 and minutes<15):
        hr = 6-hours
    elif(
            (hours>=6 and minutes>15 or hours>6)
            and (hours<22 or hours==22 and minutes<15)
            ):
        hr = 22-hours
    else:
        hr = 30-hours
    sr = 60-seconds
    
    mr = 15-minutes
    if mr<0:
        hr -= 1
        mr += 60
    
    print("{}:{}:{}      ".format(hr, mr, sr), end="\r")

    time.sleep(1)
