# def mysum(*args):
#     sum1=0
#     for i in args:
#         sum1=sum1+i
#     return (sum1)
# print(mysum(1,2,3,4,5,6,7))
# print(mysum(1,2))
#
# def largestNumber(*numbers):
#     m=numbers[0]
#     for num in numbers:
#         if num>m:
#             m=num
#     print("largest:",m)
# largestNumber(1,2,3,4,5)
#
# tax=lambda salary:salary*20/100
# salary=int(input("enter your salary:"))
# print("tax to be paid is",tax(salary))
#
# doublenum=lambda x:x*2
# a=int(input("a: "))
# print(doublenum(a))
#  x=lambda a,b:a*b
#  print(x(5,6))
# def squares(x):
#     return x**2
# list1=[1,2,3,4,5]
# print(list(map(squares,list1)))
# print(list(map(lambda x:x**2,list1)))
# print([x**2 for x in list1])

# filter function

# a= [1,2,3,5,7,9,8]
# b= [2,4,5,7,8]
# print(list(filter(lambda x:x in a,b)))
# print([x for x in a if x in b])

# a=[1,2,3,6,7,9]
# b=[3,5,8,9,4,1]
# print(list(filter(lambda x:x is not in a,b)))
# print([x for ])

def largestinthree(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
#
# num1=int(input("enter the num1:"))
# num2=int(input("enter the num2:"))
# num3=int(input("enter the num3:"))
# result=largestinthree(num1,num2,num3)
# print("largest of the value entered is",result)

# def computeGCD(x,y):
#     if x>y:
#         small=y
#     else:
#         small=x
#     for i in range(1,small+1):
#         if((x%i==0)and(y%i==0)):
#             gcd=i
#     return gcd
# a=int(input("x:"))
# b=int(input("y:"))
# print(computeGCD(a,b))

# function in function
# def square(x):
#     x=x*x
#     return x
# def double(x):
# #     x=x*2
# #     return x
# # num=int(input("num:"))
# # print("double,squaring the value:",square(double(num)))
#
# def compose(*functions):
#     def inner(arg):
#         for f in reversed(functions):
#             arg=f(arg)
#         return arg
#     return inner
# def square(x):
#      return x**2
# def increment(x):
#     return x+1
# def half(x):
#     return x/2
# composed=compose(square,increment,half)
# print(composed(5))
# composed=compose(square,increment)
# print(composed(5))
#
# def compose(*function):
#     def inner(arg):
#         for f in reversed(function):
#             arg=f(arg)
#         return arg
#     return inner
# def add(x):
#     return x+x
# def sub(x):
#     return x-x
# def mul(x):
#     return x*x
# def div(x):
#     return x/x
# composed=compose(add,sub,mul,div)
# print(composed(6))














































































































