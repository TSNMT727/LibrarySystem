import controller

def sign_up():
    while True:
        
        try:
            print("Enter your student ID:")
            new_user_id = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if controller.compare_new_member(new_user_id):
            print("User is already a registered user!")
        else:
            print("Enter member's name: ")
            name = input()

            print("Enter member's contact information (e.g., email address): ")
            contact = input()

            new_member_info = f"{new_user_id},{name},{contact},1\n"
            if controller.save_member_to_file(new_member_info):
                print(f"{new_user_id} has been registered!")

        # Ask user what to do next
        print("\nWhat would you like to do next?")
        print("1. Register another user")
        print("2. Return to main menu")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '2':
            # TODO: go to main_menu
            break
        elif choice != '1':
            print("Invalid option. Returning to main menu by default.")
            # TODO: go to main_menu
            break

def display_members():
    members_JSON = controller.read_members_from_file()
    print(members_JSON)
    # TODO: Something-something make this prettier something-something ahh idk...
