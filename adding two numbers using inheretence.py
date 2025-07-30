'''
code to perform adition operation using super class as user input ad sub class as operation 
print the sumated value at subclass
'''
class operate:
    def user_data(self):
        self.n1=int(input("Enter the value of num-1:"))
        self.n2=int(input("Enter the value of num-2:"))
class summated(operate):
    def add(self):
            res=self.n1+self.n2
            print(f"result : {res}")
        

c=summated()
c.user_data()
c.add()