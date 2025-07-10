#wap to find to find remainer when a number is divided by z

z=2
print(11%2)

#check the type of the variable assigned using input() function.

base = int(input("Enter any number: "))
for i in range (1,11):
  result = base * i;
print(f"{base} * {i} = {result}")


#use compariosn operator to find out whether a given variable a is greater than b or not 
 
a = 34
b = 80
result = a > b
print(f"{a} is greater than {b} : {result}")

#wap to find average of twos numbers enetered by users

a = int (input("Enter first number:"))
b = int(input("Enter sencond number:"))
average = (a+b/2)
print(f" {a} and {b} average is {average}")

#wap to find the square of a number entered by user
a = int(input("Enter a number: "))
square = a * a
print(f"{a} square is {square}")

#wap to display a user entered name followed by Good Afternoon using input() function.
name = input("Enter your name: ")
print(f"Good Afternoon {name}!")



name = input("Enter your name: ")
date = input("Enter the date: ")

#
letter = """Dear <|NAME|>,
You are selected!
Date: <|DATE|>
"""


letter_filled = letter.replace("<|NAME|>", name)
letter_filled = letter_filled.replace("<|DATE|>", date)


print("\nHere is your letter:\n")
print(letter_filled)