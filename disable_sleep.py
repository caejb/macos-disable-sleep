import os
from time import sleep

def start():
    os.system('clear')
    choise = input("""Sleep Management Tool 
                        (enable/disable)""")
    tool(choise)

def x(choise):
    sleep(2)
    os.system('clear')

def tool(choise):
    if choise == "disable":
        os.system("sudo pmset -a disablesleep 1")
        print("Sleep disabled")
        x()
    elif choise == "enable":
       os.system("sudo pmset -a disablesleep 0")
       print("Sleep enabled")
       x()
    else:
       print("Invalid choise, please write enable or disable")
       x()
       start()

if __name__ == "__main__":
    start()
