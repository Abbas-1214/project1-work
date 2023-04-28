class main:
    def __bills(self):
        print("Assalam-o-Aalikum")
    def __init__(self):
        pass
    def __clear(self):
        pass
    def __getname(self):
        return self.__products
        return self.__bread
        return self.__wheat

class employee(main):
    def __bills(self):
        super()._main__bills()
        print("Bills")
    def __init__(self):
        self.__honey=0
        self.__products=0
        self.__bread=0
        self.__wheat=0

    def __clear(self):
        self.__honey=int(input("enter the amount of honey: "))
        self.__products=int(input("enter the amount of product: "))
        self.__bread=int(input("enter the amount of bread: "))
        self.__wheat=int(input("enter the amount of wheat: "))
        print(f" the total bill  is {self.__products} {self.__bread} and {self.__wheat} {self.__honey}")
        print(f"the sum is : {self.__products+self.__bread+self.__wheat+self.__honey} ")
    def __getname(self):
        return self.__honey
    
    def output(self):
        self.__clear()
        

customer2=employee()
s=[]
n=int(input("enter the number of program runs:"))
for i in range(0,n):
    customer2=employee()
    s.append(customer2)
for i in s:
    i.output()

