import time

current_time = time.strftime('%H:%M:%S')

if(current_time < "12"):
    print("Good Morning!")
elif(current_time < "17"):
    print("Good Afternoon!")
elif(current_time < "20"):
    print("Good Evening!")
else:
    print("Good Night!")