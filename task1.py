#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades
It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
                eg: 
    st1.showGrade(0)
        English 91
    st2.showGrade(1)
        Math 98
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
 
    name = ""
    studentID = ""
    grade = ""
    courses = []
    grades = []

    # properties should be listed first

    def __init__(self,name,studentID,grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentID = studentID
        self.grade = grade
    
    def showGrade(self,posision):
        prt1 = self.courses[posision]
        
        prt2 = self.grades[posision]

        prt3 = str(prt1 + " " + str(prt2))
        return prt3
        


    def getGrades(self, inputList):
        # the grades are stored in self.grades
        # receives a list as input
        # input list now contains all the information in a local variable
        self.grades = inputList
        

    def getCourses(self,x):
        self.courses = x
        

    def whoAmI(self):
        print( self.name)

    def average(self):
        sum_grades = 0
        for t in self.grades:
            sum_grades = sum_grades + t           

        avg = sum_grades / len( self.grades )
        return avg
    def getHonorRoll(self):
        y = list(self.grades)
        y.sort()
        y.pop(0)
        y.pop(0)
        sum_grades = 0
        for t in y:
            sum_grades = sum_grades + t
        
        y = sum_grades / len( y )
        if y >= 86:
            return True
        else:
            return False

        

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73] )

    print( st1.getHonorRoll() )

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71] )



main()
