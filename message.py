import pyautogui as spam
import time 

limit = int(input("no. of messages "))
msg = input('message ')

time.sleep(10)

for type in range(limit):
    spam.typewrite(msg)
    spam.press("enter")