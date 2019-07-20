#!/usr/bin/python
import sys
#Number
#strings

a=9
b=8.2
c=0b1010
d=0xa
e="Hello"

if a==9:
    print("9 Matched")
if b == 8.2:
    print("8.2 matched")
if c == 10:
    print ("10 matched")
if d== 10:
    print ("10 Matched")
if e=="Hello":
    print ("hello Matched")
    
    
#use of else if similar switch case statement in c 
print("Start else if testing")

if a==7:
    print("9 Matched")
elif b == 8.1:
    print("8.2 matched")
elif c == 11:
    print ("10 matched")
elif d== 10:
    print ("10 Matched")
elif e=="Hello":
    print ("hello Matched")

#True is keyword  True =1    
 

#while True:
    print ("True case")
    

#looping constructs in Python 
#for loop 
# 
list=[1,2,3,4]
list1=[5,6,7,8]
for val in list:
  print("val is")
  print(val)
  for val1 in list1:
    print("val1 is")
    print(val1)
    if val1==7:
        print("7 found")
        #break to come out of for loop
        continue        
    print (val)

print("While loop")    
l=len(list)
i=1
#while doesnt iterate automatically
while i< l:
    print(list[i])
    i=i+1
    

    
#Data structure
#List
#
#List,Tuples,Dictionaries,Sets

list=[11,12,13,14,15,16,17]

#accessing list element is like array  list[0] list [1]....

print (list[0])

#find length of list
print(len(list))

#negative index   negative index starts from right most side -1 ,-2,-3  right to left
print(list[-1])
print(list[-2])
#-6 is not valid index
#print(list[-6])


    
    

    
    
#slicing of list  m:n m<n starts from m and ends at n  from 2nd element to 4th element
print(list[2:5])
#negative slice

print(list[-3:-1])

#reverse traversal is not possible
print(list[::-1])
print("using reverse function")
#every thing is object object.function to access the function   in OOPS    
list.reverse()
print(list)

#append element in list 
list.append(20)
list.insert(2,99)

print (list)

#will pop the last element of list similar to stack 
print(list.pop())

if list.__contains__(99):
    print("true:99")