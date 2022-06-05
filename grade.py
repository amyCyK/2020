from Student import Student
from Student121 import Student121
import fileinput
import matplotlib.pyplot as plt
import sys
from idlelib.run import manage_socket

studentList = []
    
def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)
      
def main():
    instructions = """\nEnter one of the following:
       1 to print the contents of input data file
       2 to print all valid input data
       3 to print all students overall mark 
       4 to print all students whose mark less than 40
       5 to plot distribution of grade
       Q to end \n"""

    while True:
        sys.stderr.flush()    
        sys.stdout.write (instructions)        
        choice = input( "Enter 1 to 5 " ) 
        sys.stdout.flush()
        
        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            listValidStudent()
        elif choice == "3":
            listGradeStudent()
        elif choice == "4":
            listfailedStudent()
        elif choice == "5":
            displayGraph()
        elif choice == "Q":
            break

    print ("End Grade Processing App")

if __name__ == "__main__":                       
    try:
        
        displayFile(sys.argv[1])
        main()
    
    except IndexError as error:
        sys.stderr.write("Type \"python grade.py filename\" to run program\n")
    except FileNotFoundError as fileNotFoundError:
        sys.stderr.write(str(fileNotFoundError)) 
#main

#item2
def listValidStudent():
    '''
    list of valid input data
    '''
    fileIn = open("markdata1.dat","r")
    line = fileIn.readline()    
    
    while line != " ": #loop to process inputfile
        try:
            if Student.numStudent == 0:
                studentList.append(Student121(line))
            else:
                studentRec = line.split("_")
                for student in studentList:
                    if student.getStudID() == studentRec[0]:
                        raise ValueError("repeating student error :")
                     
                studentList.append(Student121(line))                
                
        except ValueError as valueError:
            sys.stderr.write(str(valueError)+' '+line)
            sys.stderr.flush()
            sys.stdout.flush()         
              
        line = fileIn.readline() 
        
    sys.stdout.write('''
Stud ID   Name        CW1 mark Test mark  CW2 mark Exam mark 
============================================================
''')
    
    for student in studentList:
        print(student)         
    fileIn.close()

def displayGraph():
    '''
    Bar chart of student grade
    '''
    fig = plt.figure(figsize=(10,8))    # width x height in inches
    ax1 = fig.add_subplot(111)
         
    gradeFeq = {"A":0,"B":0,"C":0,"D":0,"F":0}
                
    ax1.set_xlabel("Grade")
    ax1.set_ylabel("Student Numbers")
    ax1.set_title("Grade Distribution")
    
    grades = []
    for student in studentList: #get the data
        score = student.overall()
        grade = ''
        if score < 0:
            grade = "?"
        elif score < 40:
            grade = "F"
        elif score < 50:
            grade = "D"
        elif score < 65:
            grade = "C"
        elif score < 75:
            grade = "B"
        elif score < 100:
            grade = "A"
        else:
            grade = "?"
        gradeFeq[grade] += 1
    ax1.bar(gradeFeq.keys(), gradeFeq.values())

    plt.show()


#item3
def listGradeStudent():
    '''
    grade list in ascending order of student name
    '''
    sys.stdout.write
    ('''
Stud ID   Name        CW1 mark Test mark  CW2 mark Exam mark    CW mark    Overall
==================================================================================
''')

    for student in sorted(studentList, key = lambda c: c.getName()):
        print(str(student)+' '+'%10.2f'%(student.getCoursework())+' '+'%10.2f'%(student.overall()))


#item4              
def listfailedStudent():
    '''
    list of students whose overall marks less than 40
    '''
    sys.stdout.write
    ('''
Stud ID   Name        CW1 mark Test mark  CW2 mark Exam mark    CW mark    Overall
==================================================================================
''')
    for student in sorted(studentList, key = lambda c: c.getName()):
        if student.overall() < 40:
             print(str(student)+' '+'%10.2f'%(student.getCoursework())+' '+'%10.2f'%(student.overall()))
        
