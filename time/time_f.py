import time


# def clock():
#     hour=time.strftime("%H")
#     minute=time.strftime("%M")
#     second=time.strftime("%S")
#     clk=hour+':'+minute+':'+second
#     print(clk)
#     return clock



# print("####################")
# while True:
#     clock()
#     time.sleep(1)











    # hour_pm_am=time.strftime('%I')
    # hour=time.strftime('%H')
    # pm_am=time.strftime('%p')
    # minute=time.strftime('%M')
    # second=time.strftime('%S')
    # day=time.strftime('%A')
    # zone=time.strftime('%Z')
    # text_time=hour_pm_am+':'+minute+':'+second+' '+pm_am+', '+ day+"   "+zone
    # return text_time

# print(clock())


def clock():
    hour_pm_am=time.strftime('%I')
    hour=time.strftime('%H')
    pm_am=time.strftime('%p')
    minute=time.strftime('%M')
    second=time.strftime('%S')
    day=time.strftime('%A')
    zone=time.strftime('%Z')
    text_time=hour_pm_am+':'+minute+':'+second+' '+pm_am+', '+ day+"   "+zone
    print(text_time)
    time.sleep(1)
    return clock()

clock()