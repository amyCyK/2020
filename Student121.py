from Student import Student

'''
Student121 class 

Created on May 18, 2020

@author: amy chan
'''
class Student121(Student):
    '''
    Student121 class to represent each 121COM student object
    '''
    CW1weight = 0.2 # class variable for weights for the coursework 1
    CW2weight = 0.2 # class variable for weights for the coursework 2 
    CW3weight = 0.6 # class variable for weights for the coursework 3
    
    CWweight = 0.7 # class variable for weights for the coursework 
    EXweight = 0.3 # class variable for weights for the exam 
       
    def __init__(self,dataLine):
        '''
        constructor method
        
        Parameters:
        - dataLine with following data feilds
            - studID: student ID
            - name: name of student
            - test: test mark
            - iAsgn: individual assignment mark
            - gAsgn: group assignment mark
            - exam: exam mark
        '''
        studentRec=dataLine.split('_')
        
        if len(studentRec) != 6:                                            #50523456_lau tai man_58.0_62.4_86.55_70.0_12.0
            raise ValueError('incorrect number of data in input line :')
        elif studentRec[0] == '' or studentRec[1] == '':                    #50323456__90.0_30.0_50.0_79.5
            raise ValueError('Invalid Student ID or Name :')
        elif float(studentRec[2]) < 0 or float(studentRec[2]) > 100 :      #50623456_chui tai man_31.0_64.5_46.0_-29.5
            raise ValueError('Invalid CW1 mark :')
        elif float(studentRec[3]) < 0 or float(studentRec[3]) > 100 :      #50623456_chui tai man_31.0_64.5_46.0_-29.5
            raise ValueError('Invalid Test mark :')
        elif float(studentRec[4]) < 0 or float(studentRec[4]) > 100 :      #50623456_chui tai man_31.0_64.5_46.0_-29.5
            raise ValueError('Invalid CW2 mark :')
        elif float(studentRec[5]) < 0 or float(studentRec[5]) > 100 :      #50623456_chui tai man_31.0_64.5_46.0_-29.5
            raise ValueError('Invalid Exam mark :')
        if len(studentRec) == 0:
            raise ValueError('empty or invalid data only :')
                
        Student.__init__(self,studentRec[0],studentRec[1])
        
        self.__test  = float(studentRec[2])
        self.__iAsgn = float(studentRec[3])
        self.__gAsgn = float(studentRec[4])
        self.__exam  = float(studentRec[5])


    def getTest(self):
        '''
        accessor method to get student test mark
        '''
        return self.__test
    
    def getIAsgmt(self):
        '''
        accessor method to get student nindividual assignment mark
        '''
        return self.__iAsgn
            
    def getGAsgmt(self):
        '''
        accessor method to get student group assignment mark
        '''
        return self.__gAsgn
    
    def getExam(self):
        '''
        accessor method to get student examination mark
        '''        
        return self.__exam   
    
    def getCoursework(self):
        '''
        accessor method to get student coursework mark
        '''              
        return Student121.CW1weight * self.getTest() + \
            Student121.CW2weight * self.getIAsgmt() + \
            Student121.CW3weight * self.getGAsgmt()
                   
    def overall(self):
        '''
        service method to calculate overall mark from the weighted sum of the coursework mark and the the exam mark
        '''
        return Student121.CWweight * self.getCoursework() + \
                Student121.EXweight * self.getExam()
           
    def __str__(self):
        '''
        String representation of student object
        '''
        return '%25s%0.2f%10.2f%10.2f%10.2f'%(Student.__str__(self),self.getTest(),self.getIAsgmt(),self.getGAsgmt(),self.getExam())
              
