import time
from datetime import datetime as dt

time_start = input("Enter to start time")
curr_time_start = time.time()
date_obj = dt.fromtimestamp(curr_time_start)
start_time_form = date_obj.strftime("%X:%f")


time_end = input("Enter to end time")
curr_time_end = time.time()
date_obj = dt.fromtimestamp(curr_time_end)
stop_time_form = date_obj.strftime("%X:%f")

elp_time = curr_time_end-curr_time_start


print("start time is ",start_time_form,"End time is ",stop_time_form,"elapsed time ",elp_time)