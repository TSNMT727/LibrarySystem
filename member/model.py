MEMBERS_FILE = "data/members.txt"

f = open(MEMBERS_FILE, "a")

def load_members():
    with open(MEMBERS_FILE, "r") as file:
        lines = file.readlines()
    
    parsed_members_JSON = convert_to_json(lines)

    return(parsed_members_JSON)

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
        

def save_member_to_file(member):
    with open(MEMBERS_FILE, "a") as file:            
        try:
            line = f"{member['id']},{member['name']},{member['contact']},{member['status']}\n"
            file.write(line)
        except Exception as e:
            return e  # return actual exception
    return True


