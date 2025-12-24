from pydantic import BaseModel
from datetime import date

class Lesson(BaseModel):
    student_id: int
    teacher_id: int
    lesson_date: date
    lesson_id: int
    
    
class Student(BaseModel):
    student_name: str
    student_id: int

class Teacher(BaseModel):
    teacher_name: str
    teacher_id: int


