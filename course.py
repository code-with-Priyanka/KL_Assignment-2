"""This is a student record registring in course"""
from fastapi import FastAPI,HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()
try:
    client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
    print("Connected to database")
except Exception as e:
     print(e.args)  
  
db = client['interns_b2_23']
lib = db['priyanka_sh']

class Student(BaseModel):
    name: str
    registration_no: int
    course_id: int
    course_name: str

# Create a new book
@app.post("/add/")
def create_book(student: Student):
    lib.insert_one(student.dict())
    return {"message": "Data inserted successfully"}

@app.get("/")
async def get_all_data():
    students =  lib.find({})
    details = []
    for document in students:
        detail = {'name':document['name'],'registration_no':document['registration_no'],'course_id':document['course_id'],'course_name':document['course_name']}
        details.append(detail)
    return {"details":details}


@app.put("/update/{id}")
async def update(id:int,student: Student):
    try:
        if list(lib.find({"registration_no": id})) == []:
            raise HTTPException(status_code=404, detail="Student does not exist")
        lib.update_one({"registration_no": id}, {"$set": student.dict()})
        return {"message": "Student data updated successfully!"}
    except Exception as e:
        return (e.args)

@app.delete("/delete/{id}")
def delete(id:int):
    result = lib.delete_one({'registration_no':id})
    print(result)
    return {"message": "Student record deleted successfully"}



