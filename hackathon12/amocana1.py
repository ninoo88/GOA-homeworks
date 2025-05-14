#Task 1: Sum of Two Numbers
#Instructions:
 #Store the sum of two numbers a and b in a variable result.
#Test Cases:
#assert result == 5 when a = 2, b = 3
#assert result == 0 when a = -1, b = 1
#assert result == 30 when a = 10, b = 20

a = 3
b = 2
result = a + b
print(result)

a = -1
b = 1
result = a + b
print(result)

a = 10
b = 20
result = a + b
print(result)


#Task 2: Boolean AND Operation
#Instructions:
#Given two boolean values a and b, store the result of a and b in result.
#Test Cases:
#assert result == True when a = True, b = True
#assert result == False when a = True, b = False


a = True
b = False
result = True or False
print(result)

a = True
b = False
result = True and False
print(result)



#Task 4: List Length
#Instructions:
# Get the length of a list and store it in result.
#Test Cases:
# assert result == 3 when list = [1, 2, 3]
# assert result == 0 when list = []

list = [1, 2, 3]
result =len(list)
print (result)

list = []
result =len(list)
print (result)


#Task 6: List Slicing
#Instructions:
# Slice the first three elements from a list and store them in the result.
#Test Cases:
# assert result == [10, 20, 30] when list = [10, 20, 30, 40, 50]
 
list = [10, 20, 30, 40, 50]
result = slice(list)
print(result)


 #Extra 1: Find the Largest Number in a List
#Instructions:
 #Given a list of numbers, find the largest number and store it in result.
# test Cases:
 #assert result == 9 when list = [3, 7, 9, 2]
 #assert result == 5 when list = [5, 3, 1]

num=[3, 7, 9, 2]
result = max(num)
print(result)

num = [5, 3, 1]
result = max(num)
print(result)
