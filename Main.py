import time
import os

def Main():
    os.system("taskkill /f /im explorer.exe")
    time.sleep(3)
    os.system("start explorer")
    time.sleep(7)
    print("This Shell is Now Restarted Successfully!!! This Script is Created by RiritoNinigaya")
    time.sleep(0.4)
    exit(551)

if __name__ == "__main__":
    Main()