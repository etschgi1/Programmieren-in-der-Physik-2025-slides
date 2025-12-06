import time
import sys
print("Multiple", "arguments", "to", "print", sep=" | ", end="!\n")
print("Countdown: ")
for i in reversed(range(10)):
    print(i, end="\r")
    time.sleep(0.5)