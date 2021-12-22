#Functions
def pos_int_input(prompt):
    var=0
    while var<=0: 
        var=input(prompt)
        try:
            var=int(var)
        except ValueError:
            var=0
        if var <= 0:
            print("Input needs to be a positive integer!")
    return var

def stay(prompt):
    while True:
        stay=input(prompt).upper()
        if stay == "Y":
            return True
        elif stay == "N":
            return False
        else:
            print("Invalid Response")

def sign_up(slot):
    print("\nParticipant Sign Up")
    print("====================")
    stay_bool=True
    while stay_bool:
        new_name=input("Input a name: ")
        new_slot=pos_int_input("What slot?: ")
        if new_name in slot.values() or new_slot>len(slot) or slot[new_slot] is not None: #Input validation
            if new_name in slot.values():
                print("That name has already been used")
            if new_slot>len(slot):
                print("That slot does not exist!")
            elif slot[new_slot] is not None:
                print("That slot has already been taken")
            stay_bool=stay("Do you still want to sign up?: ")
        else:
            slot[new_slot]=new_name
            return True
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Welcome Screen
print("Welcome to Tournaments R Us")
print("===========================")
part_num=pos_int_input("Enter the number of participants: ")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Initialization
starting_slot={}
for i in range(1,part_num+1):
    starting_slot[i] = None

unsaved_changes=False
print(len(starting_slot))
#-----------------------------------------------------------------------------------------------------------------------------------------------
#Menu
print("""\nParticipant Menu
================
1. Sign Up
2. Cancel Sign Up
3. View Participants
4. Save Changes
5. Exit""")
menu_option=pos_int_input("")

if menu_option==1:
    if sign_up(starting_slot):
        unsaved_changes=True
elif menu_option==2:
    print("hi")
elif menu_option==3:
    print("hi")
elif menu_option==4:
    print("hi")
elif menu_option==5:
    print("hi")    