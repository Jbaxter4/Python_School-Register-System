from tkinter import *
import tkinter.messagebox as tm
from tkinter import font
from datetime import date
import os

# Requires class folders be created beforehand

def getAttendance(height, attendance, students, subject, studentClass):
    error = False
    for i in range(height):
        if error == False:
            entry = attendance[i].get()
            if not (entry == "P" or entry == "X" or entry =="/"):
                error = True
    if error == True:
        tm.showinfo("Error", "All entries should be P, X, or /.")
    else:
        attendanceDate = date.today()
        attendanceDate = attendanceDate.isoformat()
        try:
            for i in range(height):
                file = "\\attendance" + "\\" + studentClass + "\\" + subject + "\\" + students[i] + ".txt"
                path = os.getcwd() + file
                file = open(path,"a")
                newList = [attendanceDate, attendance[i].get()]
                print(newList, file=file)
                file.close()
            tm.showinfo("Saving...", "Saved Successfully!")
        except:
            print("Error adding attendance")

def window(subject, studentFile, studentClass):
    att_window = Toplevel()
    att_window.title("Attendance")
    file = open(studentFile, "r")
    n = 0
    for line in file:
        n += 1
    height = n
    file.close()
    width = 2
    file = open(studentFile, "r")
    attendance = {}
    students = {}
    headerFont = font.Font(size=9, weight='bold')
    Label(att_window, text="P = Present, X = Absent, / = Absent without reason ").grid(row=0, column=0, columnspan=2)
    Label(att_window, text="Name", font=headerFont).grid(row=1, column=0)
    Label(att_window, text="Attendance", font=headerFont).grid(row=1, column=1)
    for i in range(height):  # Rows
        for j in range(width):  # Columns
            if j == 0:
                students[i] = file.readline()
                students[i] = students[i][:-1]
                b = Label(att_window, text=students[i])
                b.grid(row=i + 2, column=j)
            if j == 1:
                attendance[i] = StringVar()
                b = Entry(att_window, textvariable=attendance[i])
                b.grid(row=i + 2, column=j)
    Button(att_window, text="Save Attendance", command=lambda: getAttendance(height, attendance, students, subject, studentClass)).grid(row=height + 3, column=0, columnspan=2)
    file.close()
