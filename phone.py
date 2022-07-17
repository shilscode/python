class employee:
    def __init__(self,age , salary,name):
        self.age=age
        self.salary=salary
        self.name=name
        
    def d_employee(self):
        print("the  emolyee's age is ", self.age)
        print("The salary of that employee is ",  self.salary)
        print ("the  name of that employee is",self.name)
        
emp1=employee(23, 20000,"Rajat Ghoshal\n")
emp2=employee(30, 50000,"Sumit Anand\n")
emp1.d_employee()
emp2.d_employee()

        
        
    
    


