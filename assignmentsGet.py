from tkinter import *
import gradesAdd

def getAssignments(assignment,subject,studentFile, studentClass):
    assignment = assignment.rstrip("\n")
    print(assignment + assignment)
    gradesAdd.window(assignment,subject,studentFile, studentClass)

def window(subject,studentFile, studentClass):
    sela = Toplevel()
    sela.geometry("400x80+200+150")
    assignment = StringVar()
    assignment.set('Select an Assignment')
    with open("assignments\\"+subject+"\\"+studentClass+".txt", "r") as file: 
        x = file.readlines()
    options = OptionMenu(sela, assignment, *x)
    options.pack(side='left', padx=10, pady=10)
    button = Button(sela, text="SELECT", command = lambda: getAssignments(assignment.get(),subject,studentFile, studentClass)) 
    button.pack(side='right', padx=20, pady=10)
