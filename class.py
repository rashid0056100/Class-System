class Student:
    Uni='Islamia Univeristy BWP'
    def __init__(self,fullname,rollno,marks):
    
        self.name=fullname
        self.rollno=rollno
        self.marks=marks
s1=Student('Rashid','8059','75')
print("Student Name:",s1.name,"\nRoll_No:",s1.rollno,"\nPysgoclogy:",s1.marks,"\n",s1.Uni)
print("\n")
s2=Student('Ali','8081','65')
print("Student Name:",s2.name,"\nRoll_No:",s2.rollno,"\nPysgoclogy:",s2.marks,"\n",s2.Uni)







        