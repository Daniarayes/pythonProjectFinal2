class Course:
    id=1
    courses=[]
    def __init__(self,course_name,course_level ):
        self.course_id=str(Course.id)
        self.courseName=course_name
        self.course_level=course_level
        Course.id+=1




    @staticmethod
    def crateCourse():

        course_name=input("Enter cousre name:")
        course_level=Student.levels()
        Course.courses.append(Course(course_name,course_level))
        print("Course add successfully!!")





    def get_course(course_id):
          for course in Course.courses:

              if course_id==course.course_id:

                  return  course

              return None



##########################################################################################################

class Student:
    id=1
    students=[]
    def __init__(self,stu_name,stu_level):
        self.id=str(Student.id)
        self.stu_name=stu_name
        self.stu_course=[]
        self.stu_level=stu_level
        Student.id+=1


##########################################################################
    @staticmethod
    def add_student():
        name = input("Enter student name: ")

        stu_level = Student.levels()

        new_student = Student(name, stu_level)

        Student.students.append(new_student)
        print("student saved successfully")
############################################################################
    @staticmethod
    def remove_student(student_id):
        for student in Student.students:
            if student_id == student.id:
                Student.students.remove(student)
                print(" Delete done successful")
                return

        print("User not exist")
###################################################################################
    @staticmethod
    def editStudent(student_id):
        for student in Student.students:
            if student_id == student.id:
                student_name = input("Enter new student name")
                student_level = Student.levels()
                student.stu_name = student_name
                student.stu_level = student_level
                print("student Updates Successfully!!")
                return None
        print("Student not exist")

############################################################################################
    @staticmethod
    def display():
        print("-------------------------------------------------")
        for student in Student.students:
            print(f"Student name {student.stu_name}")
            print(f"student level:{student.stu_level}")

            print(f"student course {Course.courses[student.id]}")
        print("-------------------------------------------------")



#############################################################################################
    @staticmethod
    def levels():
        while True:
            Student.stu_level=input("Enter level from {A,B,C}:")
            level_list=['a','A','B','b','C','c']
            if Student.stu_level in level_list:
                break
        return Student.stu_level




##################################################################################
    def add_new_course (self,course):

        if self.stu_level==course.course_level:
            for i in self.stu_course:
                if i.course_id ==course.course_id:
                    print("Course already exist  !!!")
                    return None

            self.stu_course.append(course)
            print("Course added successfully!!")

############################################################################################

    @staticmethod
    def add_course_to_student(student_id):
        for student in Student.students:
            if student_id == student.id:
                 course_id=input("Enter Course Id")
                 course =Course.get_course(course_id)

                 if course:

                     student.add_new_course(course)
                     return None

        print("student not exist!!")

#############################################################################
while True:
    print("Select Choice please :\n 1.Add new student \n 2.Remove Student \n 3.Edit student \n 4.Display All students \n 5.Create New course \n 6. Add course to student \n 7.Exit  ")
    print("-------------------------------------------------------------------------------------------------")
    choice =int(input("Enter a choice :"))

##########################################################################3333
    if choice ==1:
       Student.add_student()

    elif  choice ==2:
        student_id=input("enter Student id:")
        Student.remove_student(student_id)
    elif choice ==3:
        student_id=input("enter Student id:")
        Student.editStudent(student_id)
    elif choice ==4:
        Student.display()
    elif choice ==5:
        Course.crateCourse()
    elif choice ==6:
        student_id =input("enter Student id:")
        Student.add_course_to_student(student_id)
    else:
        exit()















