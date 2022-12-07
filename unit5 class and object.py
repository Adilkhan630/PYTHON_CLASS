# #self is not a key word
# the self is always  reffer to the current  instance of the classmethodin
# in the init method self refer to the newly created object and
# in the other class method it is reffer to the current init the object whose method is call
# class employee:
#     employeeid ="none"
#     employeename="none"
#     employeesalary="none"
#     employeeemail="none"
#
# def __inti__method(self,id,name,salary,email):
#     self.employeeid=12345
#     self.employeename="kchsdu"
#     self.employeesalary=199937
#     self.employeeemail="ahjaj@gmail"
# print()
#
# class student:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email
# stud_1=student("sriram",25,'ram@gmail')
# stud_2=student("adui",22,'audi@gmail')
#
# class book:
#     name='none'
#     author='none'
#     def getBookDetails(self):
#         self.name=input("enter book name")
#         self.author=input("enter author name")
#     def setBookDetails(self):
#         a=self.name
#         b=self.author
#         print("name :",a,"\n",'author : ',b)
#     def Display(self,name,author):
#         print("name : ", self.name, "\n", 'author : ',self.author)
# obj=book()
# #obj.getBookDetails()
# #obj.setBookDetails()
# obj.Display('let us c',"Yashwant Kanitkar")

#
# class car:
#     def setName(self,name):
#         self.name="name"
#     def getName(self):
#         return self.name
# honda=car()
# carname=input("car name: ")
# honda.setName(carname)
# print("honda car name:",honda.getName())
#
# class student:
#     def method1(self,name=None,wish=None):
#         print(name,wish)
# obj1=student()
# obj1.method1()
# obj1.method1("Adil")
# obj1.method1("Adil","Good Morning")



#        Inheritance
# class parent:
#     def method1(self):
#         print("Parent")
# class child(parent):
#     def method2(self):
#         print("child")
# obj1 = child()
# obj1.method1()
# obj1.method2()
# obj2=parent()
# obj2.method1()
# obj2.method1()
#
# class Animal:
#     def speak(self):
#         print("Animal Speaker")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
#
#
# #multilevel inheretance
# class Animal:
#     def speak(self):
#         print("Animal Speaker")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# class DogChild(Dog):
#     def eat(self):
#         print("Eatint bread")
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()
#
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,calculation2):    #(mulitiplaction method of inheretance)
#      def Divide(self,a,b):
#          return a/b
# d=Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(100,200))
# print(d.Divide(100,20))
#
#
# #  herarical inharetance
# class SuperClass:
#     x=3
# class SubClass1(SuperClass):
#     pass
# class SubClass2(SuperClass):
#     pass
# class SubClass3(SuperClass):
#     pass
# a=SubClass1()
# b=SubClass2()
# c=SubClass3()
# print(a.x,b.x,c.x)
#
# class one:
#     x=20
#     def fun1(self):
#         print(self.x)
# class two(one):
#     y=200
#     def fun2(self):
#         print(one.x+self.y)
# t1=two()
# t1.fun1()
# t1.fun2()
#
# class one:
#     x=30
#     def fun1(self):
#         print(one.x)
# class two(one):
#     x=40
#     y=200
#     def fun2(self):
#         print(self.x+self.y)
# t1=two()
# t1.fun1()
# t1.fun2()
#
# #multi inharetance
#
# #class input():
# #     a=None
# #     b=None
# #     c=None
# #     def data(self):
#         Input.a=int(input("enter a"))
#         Input.b=int(input("enter b"))
# class Sum(Input):
#     def add(self):
#         Input.c=Input.a+Input.b
#         print(Input.c)
# class Avg(Sum):
#     def av(self):
#         print((Input.c)/2)
# d=Avg()
# d.data()
# d.add()
# d.av()

# class book:
#     tittle=None
#     price=None
#     def getBookDetail(self,tittle,price):
#         self.tittle=tittle
#         self.price=price
#         print("Tittle : ",tittle, "\n","Price : ",price)
# class publisher(book):
#     publisherName=None
#     address=None
#
# obj1=publisher
# bookTittle=input("enter book name : ")
# bookprice=int(input("enter price of book"))
# obj1.getBookDetail(bookTittle,bookprice)
# obj1.getpubli
# sherDetail()

#print("parent")


# class a: way of writting attribute
#     x=20     #publiattribute
#     _y = 30  # protected
#     __z = 40  # private attribute
# #
#
# class a:
#     __x=20
#     def fun1(self):
#         print(self.__x)
#
# obj1=a()
# obj1.fun1()
# class a:
#     __x=20
#     _y=30
#     z=40
#     def fun1(self):
#         print(self.__x,self._y,self.z)
#
# obj1=a()
# obj1.fun1()
# print(obj1.z)
# print(obj1._y)
# #print(obj1.__x)

class one:
    __x=20
    def fun1(self):
        print(self.__x)
class two(one):
    y=200
    def fun2(self):
        print(one.x+self.y)
t1=two()
t1.fun1()
#t1.fun2()

class Student:
    __name=None
    _roll=None
    _branch=None
    # constroctor
    def __init__(self,name,roll,branch):
        self.__name=name
        self._roll=roll
        self._branch=branch
    def _display(self): #protected member dunction
        print("Name: ",self.__name)  #accessing protected data
        print("Branch: ",self._branch)
class Nerd(Student):  #Derived class
    def __init__(self,age,name,roll,branch):
        self.age=age
        Student.__init__(self,name,roll,branch)
    def displayDetails(self):
        print("Age: ",self.age,"\n","roll no: ",self._roll)
        self._display()             #calling the function of base class
obj=Nerd(23,"R2J",174349,"Information Techonalgy")
obj.displayDetails()










































