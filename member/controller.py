from tabulate import tabulate
import member.model as m

def handle_sign_up():
    while True:
        
        try:
            print("Enter your student ID:")
            new_user_id = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if m.compare_new_member(new_user_id):
            print("User is already a registered user!")
        else:
            print("Enter member's name: ")
            name = input()

            print("Enter member's contact information (e.g., email address): ")
            contact = input()

            new_member_info = f"{new_user_id},{name},{contact},1\n"
            if m.save_member_to_file(new_member_info):
                print(f"{new_user_id} has been registered!")

        # Ask user what to do next
        print("\nWhat would you like to do next?")
        print("1. Register another user")
        print("2. Return to main menu")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '2':
            break
        elif choice != '1':
            print("Invalid option. Returning to main menu by default.")
            break

def handle_list_members():
    members = m.load_members()
    if len(members) == 0:
        print("No members found")
    else:
        rows = []
        for member in members:
            row = []
            for key in member.keys():
                row.append(member[key])
            rows.append(row)

        headers = [key.upper() for key in members[0].keys()]
        print(tabulate(rows, headers, tablefmt="rounded_grid"))
    
def handle_get_member(_member_id: str):
    return m.get_member(_member_id)