import time as t
##this will enable to utilize specified functions within time library such as sleep()
##Asking user the duration for which the user wants to delay the process
seconds = int(input("How many seconds to wait"))
##Let's use a ranged loop to create the counter
for i in range(seconds):
print(str(seconds-i) + " seconds remaining \n")
##we also need the loop to wait for 1 second between each iteration
t.sleep(1)
print("Time is up")
