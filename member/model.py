import json

MEMBERS_FILE = "LibrarySystem/data/members.txt"

def read_members_from_file():
    with open(MEMBERS_FILE, "r") as file:
        lines = file.readlines()
    
    parsed_members_JSON = convert_to_json(lines)

    return(parsed_members_JSON)

def convert_to_json(data):
    lines = [line.strip().split(",") for line in data]
    members = []
    for line in lines:
        members.append({
            "stu_ID": line[0],
            "stu_Name": line[1],
            "stu_Contact": line[2],
            "stu_Status": line[3]
        })

    return(members)

def compare_new_member(new_Member):
    members_List = read_members_from_file()
    for member in members_List:
        member_stu_ID = int(member["stu_ID"])
        if new_Member == member_stu_ID:
            return (True, "Student has already been registered before!")
    
    return (False)
        

def save_member_to_file(member):
    with open(MEMBERS_FILE, "a") as file:            
        try:
            line = f"{member['stu_ID']},{member['stu_Name']},{member['stu_Contact']},{member['stu_Status']}\n"
            file.write(line)
        except Exception as e:
            return e  # return actual exception
    return True


