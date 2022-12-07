# # a=(1,2,3,4)
# # print(type(a))
# # print(a)
# # print(list(a))
# # print(type(a))
# # a=list(a)
# # print(a)
# # print(type(a))
# #tuple to list
# # a=(1,2,3,4,[10,20],4)
# # print(type(a))
# # a[4][0]=10
# # print(list(a))
# # #list to tuple
# # l1=[1,2,3,4]
# # print(tuple(l1))
#
# #dictonary
# # dict={"one":1,"two":2}
# # print(dict)
# # print(type(dict))
# # print(dict["one"])
# #
# # month={"jan":1,"feb":2,"march":3}
# # print(month)
# # print(type(month))
# # print(month.get("apr"))
# # mydict={"game":"chess","dish":"chiken","place":"home"}
# # print(mydict.get("game"))
# # print(mydict["dish"])
#
# # a={"1":"one","2":"two"}
# # print(a.get("1"))
# # (a["1"])="xyz"
# # print(a)
# #
# # d=dict([("one",1),("two",2)])
# # print(type(d))
# # print(d)
# #
# # #delet function in dictionary
# # a={"one":1,"two":2,"three":3}
# # del(a["two"])
# # print(a)
# # list1=[10,20,30]
# # result=zip(list1)
# # print(result)
# # list1=[40,30,10]
# # list2=["ten","twenty","thirty"]
# # dict1=dict(zip (list1,list2))
# # print(dict1)
# # print(sorted(dict1))
# # print(sorted(dict1.items()))
#
# # data1=input("data1:")
# # data2=input("data2:")
# # list1=data1.split(",")
# # list2=data2.split(",")
# # mydict=dict(zip(list1,list2))
# # print("list1:",list1)
# # print("list2:",list2)
# # print("dictonary:",sorted(mydict.items))
#
# # data1=input("data1:")
# # data2=input("data2:")
# # l1=data1.split(",")
# # l2=data2.split(",")
# # d1={}
# # if(len(l1)==len(l2)):
# #     for i in range(len(l1)):
# #         d1[l1[i]]=l2[i]
# #         print(sorted(d1.items()))
# #     else:
# #         print("length should be equal")
# data1=input("data:")
# data2=input("data2:")
# list1=data1.split(",")
# list2=data2.split(",")
# dict1=dict(zip())

#Program to create dictionary of items and occurences
# seq = input("seq: ")
# list1 = seq.split(",")
# for i in range(len(list1)):
# 	list1[i] = int(list1[i])
# tuple1 = tuple(list1)
# d = dict()
# for element in tuple1:
# 	if element not in d:
# 		d[element] = 1
# 	else:
# 		d[element] += 1
# print("sorted dictionary:", sorted(d.items()))

# data1 = input("data1: ")
# data2 = input("data2: ")
# list1 = data1.split(",")
# list2 = data2.split(",")
# dict1 = dict(zip(list1, list2))
#
# data3 = input("data3: ")
# data4 = input("data4: ")
# list3 = data3.split(",")
# list4 = data4.split(",")
# dict2 = dict(zip(list3, list4))
#
# kv = input("key: ")
# if(kv in dict1.keys() and kv in dict2.keys()):
# 	print("key present in both dictionaries")
# elif(kv in dict1.keys()):
# 	print("key present in first dictionary")
# elif(kv in dict2.keys()):
# 	print("key present in second dictionary")
# else:
# 	print("key is not present")

# a = input("data1: ")
# b = input("data2: ")
# a = a.split(',')
# b = b.split(',')
# d = dict(zip(a,b))
# print("dictionary with key order")
# for key,value in sorted(d.items()):
# 	print(key,value)
# f = dict(zip(b,a))
# print("dictionary with value order")
# for key,value in sorted(f.items()):
# 	print(key,value)
# list comphirihansion
#
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
#
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)
#
# list1=[int(x) for x in input("data: ").split()]
# print("contents;",list1)
#list comprehesions
l1=[a for a in range(50) if a%2==0 if a%3==0]
print(l1)
#without dictionary comprehesions
square_dict=dict()
for num in range(1,11):
    square_dict[num]=num*num
print(square_dict)

#dictionary comprehension
square_dict={num:num*num for num in range(1,11)}
print(square_dict)

ordchar={x:chr(x) for x in range(65,91)}
print(sorted(ordchar.items()))

























