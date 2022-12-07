# start:stop:step
#lang="Python"
#print(lang[:-2:])
# print(lang[::-2])
# print(lang[::-1])
#lang="python"
# print(lang[3:-1])
#print(lang[:-4:-1])

# str=input("input: ")
# if len(str)>2:
#     print("output:",str[:2]+str[-2:])
# else:
#     print("output:",str)

# p=float(input("p:"))
# p_1=("%.6f"%p)
# q=int(input("q:"))
# product=p*q
# prod=("%.7f"%product)
# print("p={},q={},product={}".format(p_1,q,prod))
# str1="hello"
# str2ing"
# print("m" in s)
# print("m"  not in s)
# ="world"
# print(str1[1]+ str2[1])
#
# s="good morning"
# print("m" in s)
# print("m" not in s)
# print("mo" in s)
# a="hello"
# b=3*a
# print(b)
#
# a="hello"
# print(a[:3]*3)
# str=input("str:")
# num=int(input("num:"))
# if num>len(str)or num<0:
#     print("num should  be positive,less then length of str")
# else:
#     print("result:",num*str[:num])

#to replace str words
# a="python"
# b="j"+a[1]
# print(b)
#a="This is python class"
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.swapcase())
# print(a.split("i"))
# print(a.center(17,'%'))
# print(a.expandtabs())
#bulian value
# c="hello"
# d="ABC"
# print(c.isupper())
# print(d.isupper())
# print(c.islower())
# print(d.islower())

# JOIN FUNCTION
# c="."
# l1=["www","google","co","in"]
# l2="yahoo"
# print(c.join(l1))
#print(c.join(l2))
#print("Is Alphabets:",c.isalpha())
#d="ABC23ab"
# print(d.isalpha())
# print(d.isalnum())
#
# d="ABC23ab@q12"
# print(d.isalnum())
# d="123"
# print("is Digit",d.isdigit())
# d="  "
# print("is space",d.isspace())
#
# d="123q"
# print("is Digit",d.isdigit())
# d=" h "
# print("is space",d.isspace())
# a="hello world"
# # str1=input("vgf")
# # str2=input("mhh")
# # print(3*[str1]+[str2])
#
# a="hello\tworld"
# print(a)
# a="hello\nworld"
# print(a)
# b="it's very\\n humidity\toutside"
# print(b)
# #repr function to ptint str as it is.
# z="hello\nworld\thello world"
# print(z)
# print(repr(z))
# questions
# str1="Big Data"
# str2="Hadoop"
# l1=len(str1)
# l2=len(str2)
# if l1==l2:
#     print("string are same length")
# elif l1>l2:
#     print(str2+str1+str2)
# else:
#     print(str1+str2+str1)
# #to find the place of string
# a="hello python"
# print(a.find("p"))
# #importing strings in pythons
# import string
# print(string.punctuation)
# print(string.digits)
# print(string.hexdigits)
# print(string.ascii_letters)
# print(string.printable)
# print(string.capwords("hello world"))
# print(string.octdigits)
# print(string.ascii_lowercase)
import string
punctuations=string.punctuation
result=""
str="list-[]\ntuple-()\nDictionary-="
for i in str:
    if i not in punctuations:
        result=result+i
print=("set of punctuations in string.punctuation is:",punctuations)
print=("string after removing all punctuation's is:",result)