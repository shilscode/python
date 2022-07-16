class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        
    def config(self):
        print("configuratiob  is " ,self.cpu,self.ram)

comp1=computer("i5","6gb")
comp2=computer("i5","4gb")
      
comp1.config()
comp2.config()