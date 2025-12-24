from fastapi import FastAPI
from models import Lesson 
from models import Student
from models import Teacher

app = FastAPI()

students = [
    Student(student_name="Sophia", student_id=1),
    Student(student_name="Mac", student_id=2),
    Student(student_name="Katie", student_id=3)
]

teachers = [
    Teacher(teacher_name="Alison", teacher_id=1),
    Teacher(teacher_name="Mike", teacher_id=2),
    Teacher(teacher_name="Drake", teacher_id=3)
]

lessons = [
    Lesson(student_id=1, teacher_id=1, lesson_date="2025-12-11", lesson_id=1),
    Lesson(student_id=2, teacher_id=2, lesson_date="2025-12-11", lesson_id=2),
    Lesson(student_id=3, teacher_id=3, lesson_date="2025-12-13", lesson_id=3),
]

@app.get("/student")
def read_student():
    return students

@app.post("/student")
def add_student(student: Student):
    students.append(student)
    return student

@app.put("/student")
def update_student(student: Student, student_id: int):
    for i in range(len(students)):
        if student_id == students[i].student_id:
            students[i] = student
            return "Student Updated"
    return "Failed to update student"

@app.delete("/student")
def delete_student(student_id: int):
    for i in range(len(students)):
        if student_id == students[i].student_id:
            del students[i]
            return "Student Successfully deleted"
    return "Failed to delete student"

@app.get("/teacher")
def read_teacher():
    return teachers

@app.post("/teacher")
def add_teacher(teacher: Teacher):
    teachers.append(teacher)
    return teacher

@app.delete("/teacher")
def delete_teacher(teacher_id: int):
    for i in range(len(teachers)):
        if teacher_id == teachers[i].teacher_id:
            del teachers[i]
            return "Teacher Successfully deleted"
    return "Failed to delete teacher"

@app.get("/lesson")
def read_lesson():
    return lessons

@app.post("/lesson")
def add_lesson(lesson: Lesson):
    lessons.append(lesson)
    return lesson

@app.put("/lesson")
def update_lesson(id: int, lesson: Lesson):
    for i in range(len(lessons)):
        if lessons[i].lesson_id == id:
            lessons[i] = lesson
            return "Lesson Successfly updated"
    return "Failed to update lesson"

@app.delete("/lesson")
def delete_lesson(id: int):
    for i in range(len(lessons)):
        if id == lessons[i].lesson_id:
            del lessons[i]
            return "Lesson Successfully deleted"
    return "Failed to delete lesson"
    
    
 