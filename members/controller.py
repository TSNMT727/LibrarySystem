# Controller should be used to modify/interact with database

import json

MEMBERS_FILE = "data/members.txt"

def read_members_from_file():
    with open(MEMBERS_FILE, "r") as file:
        lines = file.readlines()
    
    parsed_members_JSON = convert_to_json(lines)

    return(parsed_members_JSON)

def convert_to_json(data):
    lines = [line.strip().split(",") for line in data]
    all_json_data = []
    for line in lines:
        line_JSON = {
            "stu_ID": line[0],
            "stu_Name" : line[1],
            "stu_Contact" : line[2],
            "stu_Status" : line[3]
        }
        line_JSON_Dumps = json.dumps(line_JSON)
        all_json_data.append(line_JSON_Dumps)

    return(all_json_data)

def compare_new_member(new_Member):
    members_List = read_members_from_file()
    for member in members_List:
        member_dict = json.loads(member)  # Convert string to dictionary
        member_stu_ID = int(member_dict["stu_ID"])
        if new_Member == member_stu_ID:
            return(True, "Student has already been registered before!")
    
    return(False)
        

def save_member_to_file(member):
    with open(MEMBERS_FILE, "a") as file:            
        try:
            file.write(member)
        except Exception:
            return(Exception)
    return(True)


