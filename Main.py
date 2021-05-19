from tkinter import *
import tkinter.messagebox as tm
from datetime import date
import gradesAdd
import attendanceAdd
import assignmentsGet
import os, fnmatch

tk = Tk()

#Main Menu -----
def mainMenu():
    tk.geometry("200x270+500+100")
    tk.title("Business")
    Label(tk, text="Log in menu").pack()
    b1user = "0"
    b2user = "1"
    b3user = "2"
    b4user = "3"
    b5user = "4"
    b1 = Button(tk, text="0. HEADMASTER", command=lambda :loginMenu(b1user),height = 2, width = 15)
    b1.pack()
    b1.config(bg="red")
    b2 = Button(tk, text="1. Mr Smith - MATH",command=lambda :loginMenu(b2user),height = 2, width = 20)
    b2.pack()
    b3 = Button(tk, text="2. Mrs O'Reilly - HISTORY", command=lambda :loginMenu(b3user),height = 2, width = 20)
    b3.pack()
    b4 = Button(tk, text="3. Mr Johnson - ENGLISH", command=lambda :loginMenu(b4user),height = 2, width = 20)
    b4.pack()
    b5 = Button(tk, text="4. Ms Walsh - GEOGRAPHY", command=lambda :loginMenu(b5user),height = 2, width = 20)
    b5.pack()
    tk.mainloop()

#Accounts -----
def teacherAccountMenu(subject):
    y = Toplevel()
    y.geometry("200x240+500+100")
    Label(y, text="TEACHER ACCOUNT").pack()
    b1 = Button(y, text="ADD GRADES", command =lambda :addGradesMenu(subject),height = 2, width = 15)
    b1.pack()
    b2 = Button(y, text="VIEW GRADES", command =lambda :viewGradesMenu(subject),height = 2, width = 15)
    b2.pack()
    Label(y, text="--------------------------------").pack()
    b3 = Button(y, text="ADD ATTENDANCE", command =lambda :addAttendanceMenu(subject),height = 2, width = 15)
    b3.pack()
    b4 = Button(y, text="VIEW ATTENDANCE", command =lambda :viewAttendanceMenu(subject),height = 2, width = 15)
    b4.pack()

def headmasterAccountMenu():
    a = Toplevel()
    a.geometry("200x180+500+100")
    Label(a, text="HEADMASTER ACCOUNT").pack()
    b1 = Button(a, text="VIEW GRADES", command = headmasterGradesMenu).pack()

#View Grades -----
def viewGradesMenu(subject):
    p = Toplevel()
    p.geometry("230x180+500+100")
    Label(p, text="Choose a class").pack()
    classA = "A"
    classB = "B"
    classC = "C"
    classD = "D"
    b1 = Button(p, text="A", command = lambda:viewGrades(subject,classA),height = 2, width = 5)
    b1.pack()
    b2 = Button(p, text="B", command = lambda:viewGrades(subject,classB),height = 2, width = 5)
    b2.pack()
    b3 = Button(p, text="C", command = lambda:viewGrades(subject,classC),height = 2, width = 5)
    b3.pack()
    b4 = Button(p, text="D", command = lambda:viewGrades(subject,classD),height = 2, width = 5)
    b4.pack()

def viewGrades(subject,studentClass):
    try:
        root = Toplevel()
        root.geometry("%dx%d+%d+%d" % (400, 80, 200, 150))
        root.title("tk.Optionmenu as combobox")
        var = StringVar(root)
        var.set('Choose assignment')
        path = ""
        path = ("grades/"+subject+"/"+studentClass+"/")
        choices = fnmatch.filter(os.listdir(path), '*.txt')
        option = OptionMenu(root, var, *choices)
        option.pack(side='left', padx=10, pady=10)
        button = Button(root, text="VIEW", command=lambda:select(var.get(),path))
        button.pack(side='left', padx=20, pady=10)
    except TypeError:
        tm.showerror("Error", "No assignments for this class in our database")

def headmasterGradesMenu():
    a = Toplevel()
    a.geometry("200x180+500+100")
    Label(a, text="VIEW GRADES").pack()
    a1 = Button(a, text="SELECT STUDENT", command = selectClass).pack()

#View Attendance -----
def viewAttendanceMenu(subject):
    p = Toplevel()
    p.geometry("230x180+500+100")
    Label(p, text="Choose a class").pack()
    classA = "A"
    classB = "B"
    classC = "C"
    classD = "D"
    b1 = Button(p, text="A", command = lambda:attendanceMenu(subject,classA),height = 2, width = 5)
    b1.pack()
    b2 = Button(p, text="B", command = lambda:attendanceMenu(subject,classB),height = 2, width = 5)
    b2.pack()
    b3 = Button(p, text="C", command = lambda:attendanceMenu(subject,classC),height = 2, width = 5)
    b3.pack()
    b4 = Button(p, text="D", command = lambda:attendanceMenu(subject,classD),height = 2, width = 5)
    b4.pack()

def attendanceMenu(subject,clas):
    p = Toplevel()
    p.geometry("230x180+500+100")
    Label(p, text="Attendance Menu").pack()
    b1 = Button(p, text="VIEW ATTENDANCE BY STUDENT", command =lambda :viewAttendance(subject,clas),height = 2, width = 30)
    b1.pack()
    b2 = Button(p, text="VIEW STUDENT ATTEND < 50%", command =lambda :viewAttendance(subject,clas),height = 2, width = 30,bg="red")
    b2.pack()

def viewAttendance(subject,studentClass):
    try:
        root = Toplevel()
        root.geometry("%dx%d+%d+%d" % (400, 80, 200, 150))
        root.title("View Attendance")
        var = StringVar(root)
        var.set('Choose student')
        path = ""
        path = ("attendance/"+studentClass+"/"+subject+"/")
        choices = fnmatch.filter(os.listdir(path), '*.txt')
        option = OptionMenu(root, var, *choices)
        option.pack(side='left', padx=10, pady=10)
        button = Button(root, text="VIEW", command=lambda:select(var.get(),path),height = 20, width = 60,bg="red")
        button.pack(side='left', padx=20, pady=10)
    except TypeError:
        tm.showerror("Error", "No attendance records for this student in our database")

#Add Grades -----
def addGradesMenu(subject):
    p = Toplevel()
    p.geometry("230x180+500+100")
    Label(p, text="Choose a class").pack()
    classA = "A"
    classB = "B"
    classC = "C"
    classD = "D"
    b1 = Button(p, text="A", command = lambda:addGrades(classA,subject),height = 2, width = 5)
    b1.pack()
    b2 = Button(p, text="B", command = lambda:addGrades(classB,subject),height = 2, width = 5)
    b2.pack()
    b3 = Button(p, text="C", command = lambda:addGrades(classC,subject),height = 2, width = 5)
    b3.pack()
    b4 = Button(p, text="D", command = lambda:addGrades(classD,subject),height = 2, width = 5)
    b4.pack()

def addGrades(clas,subject):
    add = Toplevel()
    add.title("Add Grades")
    studentFile = ""
    if clas == "A":
        studentFile = "A.txt"
    if clas == "B":
        studentFile = "B.txt"
    if clas == "C":
        studentFile = "C.txt"
    if clas == "D":
        studentFile = "D.txt"
    addGradesWindow(subject, studentFile, clas)

def addGradesWindow(subject, studentFile, studentClass):
    assignmentsGet.window(subject,studentFile, studentClass)

#Add Attendance -----
def addAttendanceMenu(subject):
    p = Toplevel()
    p.geometry("230x180+500+100")
    Label(p, text="Choose a class").pack()
    classA = "A"
    classB = "B"
    classC = "C"
    classD = "D"
    b1 = Button(p, text="A", command = lambda:addAttendance(classA,subject),height = 2, width = 5)
    b1.pack()
    b2 = Button(p, text="B", command = lambda:addAttendance(classB,subject),height = 2, width = 5)
    b2.pack()
    b3 = Button(p, text="C", command = lambda:addAttendance(classC,subject),height = 2, width = 5)
    b3.pack()
    b4 = Button(p, text="D", command = lambda:addAttendance(classD,subject),height = 2, width = 5)
    b4.pack()

def addAttendance(clas,subject):
    studentFile = ""
    if clas == "A":
        studentFile = "A.txt"
    if clas == "B":
        studentFile = "B.txt"
    if clas == "C":
        studentFile = "C.txt"
    if clas == "D":
        studentFile = "D.txt"
    addAttendanceWindow(subject,studentFile,clas)

def addAttendanceWindow(subject, studentFile, studentClass):
    attendanceAdd.window(subject,studentFile, studentClass)

#Login -----
def loginMenu(user):
    username = user
    login= Toplevel()
    login.geometry("200x90+500+100")
    password = StringVar()
    login.label_1 = Label(login, text="Password")
    login.entry_1 = Entry(login,textvariable=password, show="*")
    login.label_1.grid(row=1, sticky=E)
    login.entry_1.grid(row=1, column=1)
    login.logbtn = Button(login, text="Login", command = lambda:logon(password, username))
    login.logbtn.grid(columnspan=2)

def logon(login, username):
    user = username
    password = login.get()
    if user == "0" and password == "headmaster":
        tm.showinfo("Login info", "Welcome HEADMASTER")
        headmasterAccountMenu()
    elif user == "1" and password == "123456":
        tm.showinfo("Login info", "Welcome Mr Smith - MATH")
        subject = "Math"
        teacherAccountMenu(subject)
    elif user == "2" and password == "123456":
        tm.showinfo("Login info", "Welcome Mrs O'Reilly - HISTORY")
        subject = "History"
        teacherAccountMenu(subject)
    elif user == "3" and password == "123456":
        tm.showinfo("Login info", "Welcome Mr Johnson - ENGLISH")
        subject = "English"
        teacherAccountMenu(subject)
    elif user == "4" and password == "123456":
        tm.showinfo("Login info", "Welcome Ms Walsh - GEOGRAPHY")
        subject = "Geography"
        teacherAccountMenu(subject)
    else:
        tm.showerror("Login error", "Incorrect password")

def select(var,path):
    sf = var
    print (sf)
    tk = Tk()
    myTextWidget = Text(tk) 
    with open(path+sf, "r") as myFile:
        myText = myFile.read()
    myText = myText.replace(",", " -")
    myText = myText.replace("'", "")
    myText = myText.replace("[", "")
    myText = myText.replace("]", "")
    myTextWidget.insert(0.0,myText) 
    myTextWidget.pack(expand=1, fill=BOTH)

def selectClass():
    a = Toplevel()
    a.geometry("200x200+600+200")
    Label(a, text="Select a Class").pack()
    classA = "A"
    classB = "B"
    classC = "C"
    classD = "D"
    b1 = Button(a, text="A", command = lambda:selectStudent(classA))
    b1.pack()
    b2 = Button(a, text="B", command = lambda:selectStudent(classB))
    b2.pack()
    b3 = Button(a, text="C", command = lambda:selectStudent(classC))
    b3.pack()
    b4 = Button(a, text="D", command = lambda:selectStudent(classD))
    b4.pack()

def selectStudent(Class):
    a = Toplevel()
    a.geometry("400x80+200+150")    
    student = StringVar(a)
    student.set('Select a Student')
    with open(Class+".txt", "r") as file:
        tk = file.readlines()   
    options = OptionMenu(a, student, *tk)
    options.pack(side='left', padx=10, pady=10)
    button = Button(a, text="VIEW", command = lambda:getDate(student.get(), Class))
    button.pack(side='left', padx=20, pady=10)

def getDate(Student, Class):
    try:
        routeE = ("grades/English/"+Class+"/")
        routeG = ("grades/Geography/"+Class+"/")
        routeH = ("grades/History/"+Class+"/")
        routeM = ("grades/Math/"+Class+"/")
        a = Toplevel()
        a.geometry("400x250+200+150")
        varE = StringVar(a)
        varE.set('Select a Date/Assignment for the English Grade')        
        choiceE = fnmatch.filter(os.listdir(routeE), '*.txt')
        choicesE = OptionMenu(a, varE, *choiceE)
        choicesE.pack(side='top', padx=10, pady=10)
        varG = StringVar(a)
        varG.set('Select a Date/Assignment for the Geography Grade')        
        choiceG = fnmatch.filter(os.listdir(routeG), '*.txt')
        choicesG = OptionMenu(a, varG, *choiceG)
        choicesG.pack(side='top', padx=10, pady=10)
        varH = StringVar(a)
        varH.set('Select a Date/Assignment for the History Grade')        
        choiceH = fnmatch.filter(os.listdir(routeH), '*.txt')
        choicesH = OptionMenu(a, varH, *choiceH)
        choicesH.pack(side='top', padx=10, pady=10)
        varM = StringVar(a)
        varM.set('Select a Date/Assignment for the Math Grade')        
        choiceM = fnmatch.filter(os.listdir(routeM), '*.txt')
        choicesM = OptionMenu(a, varM, *choiceM)
        choicesM.pack(side='top', padx=10, pady=10)
        button = Button(a, text="VIEW", command = lambda:addSubject(Student, routeE, routeG, routeH, routeM, varE.get(), varG.get(), varH.get(), varM.get()))
        button.pack(side='top', padx=20, pady=10)
    except TypeError:
        tm.showerror("Error", "No assignments for this class in our database")

def addSubject(student, routeE, routeG, routeH, routeM, varE, varG, varH, varM):
    vE = varE
    vG = varG
    vH = varH
    vM = varM
    myTextE = ""
    myTextG = ""
    myTextH = ""
    myTextM = ""
    with open(routeE+vE, "r") as myFileE:
        for line in myFileE:              
            line = line.replace(",", "")
            line = line.replace("'", "")
            line = line.replace("[", "English: ")
            line = line.replace("]", "")
            if student in line:
                myTextE = line
                myTextE = line.replace(student, "\n")

    with open(routeG+vG, "r") as myFileG:
        for line in myFileG:              
            line = line.replace(",", "")
            line = line.replace("'", "")
            line = line.replace("[", "Geography: ")
            line = line.replace("]", "")
            if student in line:
                myTextG = line
                myTextG = line.replace(student, "\n")

    with open(routeH+vH, "r") as myFileH:
        for line in myFileH:              
            line = line.replace(",", "")
            line = line.replace("'", "")
            line = line.replace("[", "History: ")
            line = line.replace("]", "")
            if student in line:
                myTextH = line
                myTextH = line.replace(student, "\n")

    with open(routeM+vM, "r") as myFileM:
        for line in myFileM:              
            line = line.replace(",", "")
            line = line.replace("'", "")
            line = line.replace("[", "Maths: ")
            line = line.replace("]", "")
            if student in line:
                myTextM = line
                myTextM = line.replace(student, "\n")            
  
    present(student, myTextE, myTextG, myTextH, myTextM)             

def present(student, myTextE, myTextG, myTextH, myTextM):
    tk = Tk()
    tk.title(student)
    myTextWidget = Text(tk)     
    myTextWidget.insert(0.0, myTextE)
    myTextWidget.insert(1.0, myTextG)
    myTextWidget.insert(2.0, myTextH)
    myTextWidget.insert(3.0, myTextM)
    myTextWidget.pack(expand=1, fill=BOTH)            

mainMenu()
