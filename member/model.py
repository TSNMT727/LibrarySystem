MEMBERS_FILE = "data/members.txt"

def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            return(convert_to_json(file.readlines()))
    except FileNotFoundError:
        open(MEMBERS_FILE, "w").close()
        return []

def get_member(member_id):
    members = load_members()
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def convert_to_json(data):
    lines = [line.strip().split(",") for line in data]
    members = []
    for line in lines:
        members.append({
            "id": line[0],
            "name": line[1],
            "contact": line[2],
            "status": line[3]
        })

    return(members)

def compare_new_member(new_Member):
    members_List = load_members()
    for member in members_List:
        member_stu_ID = int(member["id"])
        if new_Member == member_stu_ID:
            return (True, "Student has already been registered before!")
    
    return (False)
        

def save_member_to_file(stu_id, stu_name, stu_contact, stu_status):
    try:
        with open(MEMBERS_FILE, "a") as file:
            line = f"{stu_id},{stu_name},{stu_contact},{stu_status}\n"
            file.write(line)
    except FileNotFoundError:
        open(MEMBERS_FILE, "w").close()
    return True
