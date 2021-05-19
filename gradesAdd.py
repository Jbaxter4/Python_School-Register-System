from tkinter import *
import tkinter.messagebox as tm
from tkinter import font
from datetime import date
import os

# Requires class folders be created beforehand

def getGrades(height, grade, assignment, students, subject, studentClass):
    error = False
    for i in range(height):
        if error == False:
            studentGrade = grade[i].get()
            if ord("F") < ord(studentGrade) or ord(studentGrade) < ord("A"):
                error = True
    if error == True:
        tm.showinfo("Error", "Grades should be A-F")
    else:
        gradeDate = date.today()
        gradeDate = gradeDate.isoformat()
        file = "\grades" + "\\" + subject + "\\" + studentClass + "\\" + gradeDate + " " + subject + " " + assignment + ".txt"
        path = os.getcwd() + file
        file = open(path, "w")
        for i in range(height):
            newList = [grade[i].get(),students[i]]
            print(newList, file=file)
        file.close()
        tm.showinfo("Saving...", "Saved Successfully!")

def window(assignment, subject, studentFile, studentClass):
    add = Toplevel()
    add.title("Add Grades")
    file = open(studentFile, "r")
    n = 0
    for line in file:
        n += 1
    height = n
    file.close()
    width = 2
    file = open(studentFile, "r")
    grade = {}
    students = {}
    headerFont = font.Font(size=9, weight='bold')
    Label(add, text="Name", font=headerFont).grid(row=1, column=0)
    Label(add, text="Grade", font=headerFont).grid(row=1, column=1)
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            if j == 0:
                students[i] = file.readline()
                students[i] = students[i][:-1]
                b = Label(add, text=students[i])
                b.grid(row=i + 2, column=j)
            if j == 1:
                grade[i] = StringVar()
                b = Entry(add, textvariable=grade[i])
                b.grid(row=i + 2, column=j)
    Button(add, text="Save Grades", command=lambda: getGrades(height, grade, assignment, students, subject, studentClass)).grid(row=height + 3, column=0, columnspan=2)
    file.close()
