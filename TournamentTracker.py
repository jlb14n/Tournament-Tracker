#Welcome Screen
print("Welcome to Tournaments R Us")
print("===========================")
part_num=0
while part_num<=0: #Prompts for the starting number of slots
    part_num=input("Enter the number of participants: ")
    try:
        part_num=int(part_num)
    except ValueError:
        part_num=0
    if part_num <= 0:
        print("Input needs to be a positive integer!")

#Initialization
starting_slot={}
for i in range(1,part_num+1):
    starting_slot[i] = None
print(starting_slot)

