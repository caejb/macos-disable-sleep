import os
from time import sleep

def start():
    os.system('clear')
    choise = input("Sleep Disabler? (enable/disable)")
    tool(choise)

def repeat(choise):
    tool(choise)

def tool(choise):
    if choise == "disable":
        os.system("sudo pmset -a disablesleep 1")
        print("Sleep disabled")
        sleep(2)
        os.system('clear')
    elif choise == "enable":
       os.system("sudo pmset -a disablesleep 0")
       print("Sleep enabled")
       sleep(2)
       os.system('clear')
    else:
       print("Invalid choise, please write y or n")
       sleep(2)
       os.system('clear')
       start()

if __name__ == "__main__":
    start()
