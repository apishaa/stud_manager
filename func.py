from util import*

def registeration(username,age,address,course,duration):
    data=read_json()
    
    temp_data={
        "sno":len(data["students"])+1,
        "name":username,
        "age":age,
         "add": address,
         "course":course,
         "duration":duration 
    }
    
    data["students"].append(temp_data)
    
    write_json(data)
    
def delete_stud(id):
        data=read_json()
        name=""
        for stud in data["students"]:
            if stud["sno"] == int(id):
                name=stud["name"]
                data["students"].remove(stud)
        i=1
        for stud in data["students"]:
            stud["sno"]=i
            i+=1
        write_json(data)
        return name
    
    
def update(sno,username,age,address,course,duration):
    data=read_json()
    name=username
    for stud in data["students"]:
        if stud["sno"]==sno:
            name=stud["name"]
            stud["name"]=username
            stud["age"]=age
            stud["add"]=address
            stud["course"]=course
            stud["duration"]=duration
            
    write_json(data)
    return name
        
    
                    
                
        
    