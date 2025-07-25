from utils.constants import MEMBERS_FILE

def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            return(convert_to_dict(file.readlines()))
    except FileNotFoundError:
        open(MEMBERS_FILE, "w").close()
        return []

def get_member(member_id):
    members = load_members()
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def convert_to_dict(data):
    lines = [line.strip().split(",") for line in data]
    members = []
    for line in lines:
        members.append({
            "id": line[0],
            "name": line[1],
            "contact": line[2],
        })

    return(members)

def compare_new_member(member_id):
    members_list = load_members()
    for member in members_list:
        if member["id"] == member_id:
            return True
    return False
        

def save_member_to_file(id, name, contact):
    with open(MEMBERS_FILE, "a") as file:
        line = f"{id},{name},{contact}\n"
        file.write(line)
