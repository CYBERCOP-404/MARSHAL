# import section Start
import os 
from time import sleep
# import section end
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
BANNER='''\033[1;32m
  __  __          _____   _____ _    _          _      
 |  \/  |   /\   |  __ \ / ____| |  | |   /\   | |     
 | \  / |  /  \  | |__) | (___ | |__| |  /  \  | |     
 | |\/| | / /\ \ |  _  \033[1;31mVerson-2.7 \033[1;32m__  | / /\ \ | |     
 | |  | |/ ____ \| | \ \ ____) | |  | |/ ____ \| |____ 
 |_|  |_/_/    \_\_|  \_\_____/|_|  |_/_/    \_\______|
'''
command_list='''
[1] ENCRIPTED FILE BY MARSHAL PRIMIUM
[2] ENCRIPTED FILE BY MARSHAL  
'''
comm ='''\033[0;31m
LOGIN ERROR ....
'''
while True:
    clear_screen()
    print(BANNER)
    print(command_list)
    CHOICE = input('\033[1;34mENTER YOUR CHOICE : ')
    if CHOICE =='1':
        os.system('python marshal_admin.py')
    elif CHOICE=='2':
        os.system('python marshal.py')
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# Developed by CYBER COP BANGLADESH
