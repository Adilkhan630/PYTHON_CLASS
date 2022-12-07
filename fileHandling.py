# fp=open("test2.txt","w")
# print(fp)
# fp.write("hello")
# fp.write("hello world")
# fp=open("text2.txt",'r')
# text=fp.read()
# print(text)
# fp.close()

#python programming to illustion
#Append vs write mode
#
# file1= open("myfile.1txt","w")
# L=["this is delhi \n","This is paris \n"," this is london \n"]
# file1.writelines(L)
# #file1.write(L)
# file1.close()
# # Append mode
# file1=open("myfile.txt","a")
# file1.write("Today \n")
# file1.close()
#
# file1.open("myfile.txt","rb")
# print("output of Readlines after appending")
# #print(files1.readline().decode("utf-8")
# print(file1.read)
# print()
# file1.close()
#06/12/2022
# fr=open("myfile1.txt","r")
# fw=open("Newfile.txt","w")
# fw.write(fr.read())
# fr.close()
# fw.close()
# fr1=open("newfile.txt",'r+')
# print(fr1.read(12))
# print(fr1.tell())
# print(fr1.write("this is the next text"))
# print(fr1.seek(12))
# print(fr1.read(1))
# print(fr1.seek(15))
# print(fr1.read(10))
# print(fr1.read())
# fr1.close()

# fin=open("myfile1.txt",'r')
# charCount=wordCount=lineCount=0
# for line in fin:
#     lineCount+=1
#     wordCount+=len(line.split())
#     charCount+=len(line)
# print("line count=",lineCount)
# print("Word count=",wordCount)
# print("Char count=",charCount)
#
# import pickle
#
# animalDict={'car:'2,'dog:'7,'lion:'4,'tiger:'9,'leapord:'11,'bear:'8,'elephant:'15}
# outfile=open('animal','wb')
# pickle.ump(animalDict,outfile)
# outfile.cose()
# fst=open("animals","rb")
# data=pickle.load(fst)
# try:
#     wile(True):
#         print(data)
#         data=pickle.load(fst)
# except:
#     print("Bye")

#try and exception

# marks={"Rahul":50,"Harsh":60,"Surash":70}
# name=input("enter name:")
# print("marks:",marks[name])
# print("name {} not in list".format(name))
# print("end of program")
#
# marks={"Rahul":50,"Harsh":60,"Surash":70}
# name=input("enter name:")
# try:
#     print("marks:",marks[name])
# except KeyError:
#     print("name {} not in list".format(name))
# print("end of program")

# a=[1,2,3]
# try:
#     print("second element",a[1])
#     print("fourth element",a[3])
#
# except IndexError:
#     print("entered index as out of range")
# except:
#     print("An error occuried ")
#
#
# try:
#     number1,number2=eval(input("enter two number,seprated by comma"))
#     result=number1/number2
#     print("Result is ",result)
# except ZeroDivissionError:
#     print("Division by zero")
# except SyntaxError:
#     print("a company may missing in the input")
# except:
#     print("something missing in the input")
# else:
#     print("No exception")
# finally:
#     print("The finally clause is excuted")

try:
    fh=open("testfile","r")
    fh.write(" this is my test file for xception handling")
except IOError:
    print("error can't find file or read data")
else:
    print("Contact written sucessfully")
#
# def checkage(age):
#     if age <0:
#         raise ValueError("age should be greter than or equal to zero")
#     print("age is valid")
# try:
#     age=int(input("age: "))
#     checkage(age)
# except ValueError as err:
#     print(err.args)
# finally:
#     print("excuted in any condition")
                # chacking the range handling
# try:
#     x=int(input("enter a number: "))
#     if x not in range(1,101):
#         raise Exception(x)
# except:
#     print(x,"is out of allowed range")
# else:
#     print(x,"is within the allowed range")

# class OurException(exception):
#     def __init__(self,message):
#         self.message=message
# class UsingUserException:
# try:
#         a=int(input("a: "))
#         b=int(input("b: "))
#         if b==0:
#             raise OurException("b should be ")      










