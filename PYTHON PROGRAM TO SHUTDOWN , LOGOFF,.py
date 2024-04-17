''' PYTHON PROGRAM TO SHUTDOWN , LOGOFF, RESTART '''

import os
choice = input(' Want to shutdown your computer? (y or n) =')
if choice == 'y' or choice == 'Y':
    os.system('shutdown /s /t 0') # here command /s /t 0 tell to shutdown computer immediately in 0 sec,also we use /r for restart computer and /l for log off.
else:
    print("We are exiting this program ")

