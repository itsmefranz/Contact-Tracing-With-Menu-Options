#- Display a menu of options
#	Menu:
#		 1 -> Add an item
#		 2 -> Search
#		 3 -> Exit (y/n)
#- Allow user to select item in the menu (check if valid)
#- Perform the selected option
#		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
#				   Use dictionary to store the info
#				   Use the full name as key
#				   The value is another dictionary of personal information
#		- Option 2: Search, ask full name then display the record
#		- Option 3: Ask the user if want to exit or retry.

print("\n┏━· • —– ٠ ✤ ٠ —– • · • —– ٠ ✤ ٠ —– • · • —– ٠ ✤ ٠ —– • ·━┓")
print ("""
    Menu
    [1] ✎ Add an item
    [2] ✔ Search
    [3] ∷ Exit (Y/N)
    """)
print("┗━· • —– ٠ ✤ ٠ —– • · • —– ٠ ✤ ٠ —– • · • —– ٠ ✤ ٠ —– • ·━┛\n") 

personal_info = {}
while True:
    def menu_program():
        menu=int(input("What would you like to do? [1-3] "))

    if menu=="1":
        personal_info={}
        name = input("Enter user's full name: ")
        age= input("Enter user's age: ")
        address= input("Enter user's home address: ")
        phone_num = input("Enter user's phone number: ")

        personal_info[name] = age, address, phone_num

        print(personal_info)
        print("Saved!")

    
    
    if menu=="3":
        while True:
            retry_exit = input("Do you wish to exit? (ㅅ´ ˘ `) Y/N: ")
            if retry_exit == "n":
                print("\n")
                menu_program()
            elif retry_exit == "y":
                print("\n.・。.・゜✭・.・✫・゜・。.・。.・゜✭・.・✫・゜・。.")
                print("See ya next time! Bye for now ◝(ᵔᵕᵔ)◜\n")
            else:
                print("\nEnter Y if you want to exit, or N to retry the program.")
                exit()

    menu_program()
        