#__________________________________________________ Basic List Operation __________________________________________________
#1. Write a Python program to create a list with the elements [10, 20, 30, 40, 50]. Then, replace the third element with 100 and print the updated list.
list=[10, 20, 30, 40, 50]
updated_list = list[2]
print(updated_list)

#__________________________________________________ List Slicing __________________________________________________
#2. Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9], write a Python program to print the first 5 elements and the last 3 elements using slicing.
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
First3=numbers[0:5]
Last3=numbers[-3:]
print(First3,Last3)

#__________________________________________________ List Comprehension __________________________________________________
#3. Write a Python one-liner using list comprehension to generate a list of squares for numbers from 1 to 10.
print()
print([x**2 for x in range(1,11)])

#__________________________________________________ Tuple Immutability __________________________________________________
#4. Given t = (1, 2, 3, 4), try modifying the second element to 10. What error do you get, and why?

#t=(1,2,3,4)
#t[1]=10
#Output:         TypeError: 'tuple' object does not support item assignment
#As tuple is immutable which means that the elements cannot be modified, it will automatically throw an error if we try to execute a code that tries to modify the original tuple.


#__________________________________________________ Tuple Unpacking __________________________________________________    
#5. Given the tuple coordinates = (4, 5), write a Python program to unpack its values into two variables x and y and print them.

print()
tuple_coordinates = (4, 5)
a , b = tuple_coordinates
print("x =",a)
print("y =",b)


#__________________________________________________ Basic Dictionary Operations __________________________________________________
#6. Create a dictionary called student with the following key-value pairs
#Then, update her age to 22 and add a new key "subject": "Math". Print the updated dictionary.


#             json
#             CopyEdit
#             "name": "Alice",  
#             "age": 21,  
#             "grade": "A"

print()
student = { "name" : "Tagoor", "age" : 21, "grade" : "A+" }
student["age"] = 22
print("dict_stdnt_wit_updtd_age = ",student)


#__________________________________________________ Dictionary Iteration __________________________________________________
#7. Given the dictionary, Write a Python program to print each student's name and their score.
#scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

print()
scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
for x in scores.items():
    print(x)


#__________________________________________________ Dictionary Key Search __________________________________________________
#8. Write a Python program to check if the key "Bob" exists in the dictionary { "Alice": 90, "John": 85, "Mark": 92 }.

print()
dictonary = { "Alice": 90, "John": 85, "Mark": 92 }
if "Bob" in dictonary:
    print("Bob exists in the given dictonary")
else:
    print("Bob does not exist in the given dictonary")


#__________________________________________________ For Loop - Sum of List __________________________________________________
#9. Write a Python program to find the sum of all elements in the list [5, 10, 15, 20, 25] using a for loop.

print()
list = [5, 10, 15, 20, 25]
y=0
for x in list:
    y+=x
print("Sum of all elements in the list = ", y)



#__________________________________________________ While Loop - Reverse Counting __________________________________________________
#10. Write a Python program that prints numbers from 10 to 1 in descending order using a while loop.

print()
number = 10
while number>=1:
    print(number)
    number -=1


#__________________________________________________ Loop with Break & Continue __________________________________________________
#11. Write a Python program that iterates through numbers from 1 to 10 but skips number 5 and stops the loop at 8.

print()
a=0
for x in range(1,11):
    if x==8:
        print(x)
        break
    elif x == 5:
        print(end='')
        continue
    else:
        print(x,end = '')



#__________________________________________________ Basic If-Else Condition __________________________________________________
#12. Write a Python program that asks the user for a number. If the number is even, print "Even Number"; otherwise, print "Odd Number"

x = int(input("Enter the input number:"))

if x == 0:
    print("Please try a different number")
elif x % 2 == 0:
    print(" The entered number is Even")
elif x % 2 == 1:
    print("The entered number is Odd")
else:
    print(" The entered number is either 0 or invalid")

#__________________________________________________ Nested If Conditions __________________________________________________
#13. Write a Python program to check if a number is positive, negative, or zero

print ()
y = int(input("Enter the input number:"))

if y == 0:
    print(" The entered number is Zero ")
elif y > 0:
    print(" The entered number is Positive")
elif y < 0:
    print("The entered number is Negative")
else: 
    print(" Please enter a valid number")

#__________________________________________________ Function with Arguments __________________________________________________
#14. Write a function multiply(a, b) that takes two numbers and returns their product. Call this function with the values 5 and 3.

def multiply(a,b):
    return a*b

print(multiply(5,4))


#__________________________________________________ Function with Default Parameter __________________________________________________
#15. Write a function greet(name="Guest") that prints "Hello, [name]!". If no argument is passed, it should print "Hello, Guest!".

def greet(name="Guest"):
    return name 
print("output when nothing is passed:     ","Hello",greet())
print("output when an argument is passed:     ", "Hello",greet("Engineer"))


def greet(name="Guest"):
    return f"Hello, {name}!"
greet()
greet("subbarao") 
