import time

timestamp = time.strftime('%H:%M:%S')
hrs_time = time.strftime('%H')
if hrs_time >= "00" and hrs_time < "05":
  print("Good Night")
elif hrs_time >= "05" and hrs_time < "12":
  print("Good Morning")
elif hrs_time >= "12" and hrs_time < "17":
  print("Good Afternoon")
elif hrs_time >= "17" and hrs_time < "20":
  print("Good Evening")
elif hrs_time >= "20" and hrs_time <= "23":
  print("Good Night")
else:
  print("Invalid Output")
