################### q1 ##########################
"""
Write script solve this: two friends are eating dinner at a restaurant. The bill comes in the 
amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 
15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then 
output a message saying "Each person needs to pay: " followed by the resulting number. 
"""


# (*** solution ***)
amount = 47.28
tip = amount * 0.15
total = amount + tip
pay_friend = total / 2
print(f"Each person needs to pay: ${pay_friend}")


################### q2 ##########################
"""
Ask user for input two numbers and divide one by another then display the result on the screen. 
"""


# (*** solution ***)
one_number = input("Enter the first number:- ")
two_number = input("Enter the second number:- ")
if one_number.isdigit() or two_number.isdigit():
    num1, num2 = int(one_number), int(two_number)
    result = num1 / num2
    print(f"Result: {result}")
else:
    print("Invalid number")


################### q3 ##########################
"""
You have the following variables  
word1 = "How" 
word2 = "do" 
word3 = "you" 
word4 = "like" 
word5 = "{}" 
word6 = "so" 
word7 = "far?" 
Combine them to display one sentence. 
"""


# (*** solution ***)
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far?"

print(f"{word5[0]} {word1} {word2} {word3} {word4} {word6} {word7} {word5[1]}")


################### q4 ##########################
"""
In Q3  
Replace? With ! in variable word7 
Use formatting  to change language from python to any other programming language  
"""


# (*** solution ***)
word5 = "{}"
new_word5 = word5.format("i love python")
print(new_word5)

word7 = "far?"
new_word7 = word7.replace("?", f"!")
print(new_word7)


################### q5 ##########################
"""
Write a Python program Ask user to input stamen and calculate the length of it . 
"""


# (*** solution ***)
statement = len(input("Enter a statement: "))
print(f"The statement has ({statement}) characters.")


################### q6 ##########################
"""
Develop calculator using python (+,-,*,/)
"""


# (*** solution ***)
num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))

print("Select operation:- ")
print("1- Add")
print("2- Subtract")
print("3- Multiply")
print("4- Divide")

choice = input("Enter choice (1/2/3/4):- ")

if choice == "1":
    print(f"Result: {num1 + num2}")
elif choice == "2":
    print(f"Result: {num1 - num2}")
elif choice == "3":
    print(f"Result: {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")
