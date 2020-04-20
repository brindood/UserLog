'''
TODO:
Implement flask usage
HTML user input
'''

#from flask import Flask
#from flask import request
#app = Flask(__name__)
from os import system
KILL_ID = "7607441150"    
lifetime_dict = {}
def __main__():    
    #app.run(host='0.0.0.0', port= 8080)  

    run1 = False
    options = "Options:\n"             + \
                  "1: Student input mode.\n\tWill run until keyphrase entered\n" + \
                  "2: Display Student Lifetime list\n" + \
                  "3: Quit Program\n" + \
                  "4: Delete Student Lifetime list\n" + \
                  "\n\nEnter desired func: " + \
                  ""
   
    choice= input(options)
    choice = int(choice)
    
    while(choice != 3):
        if(run1 == True):            
            choice= input(options)
            choice = int(choice)            
        if choice == 1:
            system("cls")
            student_mode(lifetime_dict)
            run1 = True
        elif choice == 2:
            print_dict_terminal(lifetime_dict)
            print("Student list printed.\n" + \
                  "Data saved into lifetime.txt.\n" + \
                  "Press Enter to end program.\n" + \
                  "Goodbye")
            run1 = True
        elif choice == 3:
            print("Quit program selected. \nPress Enter to end program. \nGoodbye")
            quit(1)
        elif choice == 4:
            verify = input("Are you really really sure you want to delete the lifetime log-in file?\n" + \
                       "If so input the titular spilled food in ''The lighthouse'' featuring  Willem Dafoe and Robert Pattinson.\n" + \
                       "Enter Now: ")
            if ((verify.lower()) == "beans"):
                f3 = open('lifetime.txt', 'r')
                f3.close()
                print("\n\tLifetime file deleted")
                run1 = True

    
    if(choice == 1):
        print("Student Read Mode Ended.\nData saved into lifetime.txt. \nGoodbye")                
            
    print("PROGRAM ENDED")
    return 0



def print_dict_terminal():
    f2 = open('lifetime.txt', 'r')
    read_in_dict(f2, lifetime_dict)
    for i in lifetime_dict:
        print(i + ": " + str(lifetime_dict[i]))
    f2.close()
    return 0

def student_mode():
    try:
        f1 = open('lifetime.txt', 'r')
        read_in_dict(f1, lifetime_dict)
        f1.close()
        read_in_users(f1, lifetime_dict)
    except:
        f1 = open('lifetime.txt', 'w')
        f1.close()
        read_in_users(f1, lifetime_dict)
    return 0
    
    
def read_in_users(f1):
    ID= ""
    while ID != KILL_ID:
        ID = input("Enter Student ID Number: ")
        if not (ID == KILL_ID):            
            print(ID + " is logged into CSIT Open Lab")
            print("Press enter to log in new user")            
            dict_insert(ID, lifetime_dict)
            input()
            system("cls")
            
    #Start print to file
    f2 = open('lifetime.txt', 'w')
    for i in lifetime_dict:
        f2.write(i + " " + str(lifetime_dict[i]) + "\n")
    f2.close()
    return 0
              
def read_in_dict(f1):
    for line in f1:
        split = line.split(" ")
        ID = split[0]
        lifetime_dict[ID] = split[1]
    f1.close()
    return 0
    
def dict_insert(ID):
    if ID in lifetime_dict.keys():
        lifetime_dict[ID] = int(lifetime_dict[ID]) + 1
    else:
        lifetime_dict[ID] = 1
    return 0
'''--------------------------------------------------------'''
#@app.route('/')
def index():
    return("Student Log In Start Page")
    
            
__main__()
