1.  # Take a number from the user and print whether it's even or odd.
a = int(input("Enter a number: "))
if a % 2 == 0:
 print("It is a Even number")
elif a % 2 == 1:
 print("It is a Odd number")

 # . Write a program to count the number of vowels in a given string.

a = input("Enter a string: ")
vowels = "aeiou"
count = 0
for char in a.lower():
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)

# Ask the user to input a sentence and print the number of words in it.
a = input("Enter a sentence:")
words = a.split()
print("Number of words in the sentence:", len(words))

# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.


def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} * {i} =  {num * i}")


num = int(input("Enter a number for multiplication table: "))
multiplication_table(num)

# Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Accept a string and check whether it is a palindrome or not (same forward and backward).
a = input("Enter a string: ")
if a == a[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break statement)
secret_number = 7
while True:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    else:
        print("Try again!")

    # Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.
even_numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)

# Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)
n = int(input("Enter the number of terms for Fibonacci sequence: "))


def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


print("Fibonacci sequence:", fibonacci(n))


# Accept a list of numbers and remove all duplicate values

a = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, a.split()))
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)