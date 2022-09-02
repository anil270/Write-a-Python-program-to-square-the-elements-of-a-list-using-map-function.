#Write a Python program to square the elements of a list using map() function.

list1 = list(map(int ,input("Enter the element of list :").split()))
list2 = list(map(lambda x:x**2,list1))
print("Before list :",list1)
print("After the list :",list2)