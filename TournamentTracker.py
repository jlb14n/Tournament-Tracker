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
            print("Error:\nInput needs to be a positive integer!")
    return var

def y_n_input(prompt):
    while True:
        y_n_input=input(prompt).upper()
        if y_n_input == "Y":
            return True
        elif y_n_input == "N":
            return False
        else:
            print("Error:\nInvalid Response")

def sign_up(slot):
    print("\nParticipant Sign Up")
    print("====================")
    stay_bool=True
    while stay_bool:
        new_name=input("Participant Name: ")
        new_slot=pos_int_input("Desired starting slot #[1-{0}]: ".format(len(slot)))
        if new_name in slot.values() or new_slot>len(slot) or slot[new_slot] is not None: #Input validation
            print("Error:")
            if new_name in slot.values():
                print("{0} is already signed up.".format(new_name))
            if new_slot>len(slot):
                print("Slot {0} does not exist.".format(new_slot))
            elif slot[new_slot] is not None:
                print("Slot #{0} is filled. Please try again.".format(new_slot))
            stay_bool=y_n_input("Do you still want to sign up? (y/n): ")
        else:
            slot[new_slot]=new_name
            return True

def cancel_sign_up(slot):
    print("\nParticipant Cancellation")
    print("========================")
    stay_bool=True
    while stay_bool:
        new_name=input("Participant Name: ")
        new_slot=pos_int_input("Desired starting slot #[1-{0}]: ".format(len(slot)))
        if new_name != slot[new_slot]:
            print("Error:")
            print("{0} is not in starting slot {1}".format(new_name,new_slot))
            stay_bool=y_n_input("Do you still want to cancel a sign up? (y/n): ")
        else:
            slot[new_slot]=None
            return True

def view_participants(slot):
    print("\nView Participants")
    print("=================")
    while True:
        start=pos_int_input("Starting slot #[1-{0}]: ".format(len(slot)))
        if start>len(slot):
            print("Error:\nSlot #{0} does not exist.".format(start))
        else:
            break
    print("\nStarting Slot: Participant")
    for i in range(start-5,start+6):
        if i<1 or i>len(slot):
            continue
        else:
            print("{0}: {1}".format(i,slot[i]))

def save_changes(slot):
    print("\nSave Changes")
    print("============")
    save=y_n_input("Save your changes to CSV? [y/n]: ")
    if save:
        print("hi")#=====================================================================================================================
        return True
    else:
        return False

def exit(slot, unsaved):
    print("\nExit")
    print("=====")
    if unsaved:
        print("Any unsaved changes will be lost.")
    y_n_input("Are you sure you want to exit? [y/n]: ")
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
while True:
    print("""\nParticipant Menu
    ================
    1. Sign Up
    2. Cancel Sign Up
    3. View Participants
    4. Save Changes
    5. Exit""")
    while True: #Input validation
        menu_option=pos_int_input("")
        if menu_option <=5:
            break
        else:
            print("That is not a valid option!")
    if menu_option==1:
        if sign_up(starting_slot):
            unsaved_changes=True
    elif menu_option==2:
        if cancel_sign_up(starting_slot):
            unsaved_changes=True
    elif menu_option==3:
        view_participants(starting_slot)
    elif menu_option==4:
        if save_changes(starting_slot):
            unsaved_changes=False
    elif menu_option==5:
        if exit(starting_slot,unsaved_changes):
            break
print("\nGoodbye!")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#troubleshooting
print(starting_slot)
print(unsaved_changes)