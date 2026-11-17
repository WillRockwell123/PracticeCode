# value = int(input("Enter an integer: "))

# if value % 2 == 0:
#     print(f'Because {value} is divisible by two, it is even.')
# value = int(input("Enter an integer: "))
# if value > 0:
#     print("The number is positive")
# code = input("Enter a letter, (A B or C): ")

# if code == 'A':
#   print("Apple")
# elif code == 'B':
#   print("Bear")
# elif code == 'C':
#   print("Cat")
# else:
#   print("Neither Apple, Bear, nor Cat") 
# age = int(input("Please enter your age: "))

# message = (
#     "You are an adult." if age >= 18
#     else "why are you on here, go outside!" if age <= 5
#     else "You are a minor."
# )

# print(message)


# number = int(input("Enter a number between 1 and 3: "))

# if number == 1:
#     print("You entered one.")
# elif number == 2:
#     print("You entered two.")
# elif number == 3:
#     print("You entered three.")
# else:
#     print("You didn't enter one, two, or three.")



# celsius = float(input("Enter the temperature in Celsius: "))
# farenheit = (celsius * 9 / 5) + 32
# print(f'The tempature in Farenheit is {farenheit}')
# if farenheit < 50:
#   print('Its cold, Wear a jacket!')
# elif 50 <= farenheit <= 77:
#   print('The weather is pleasant.')
# elif farenheit > 80:
#   print("Its hot. Stay hydrated!")

# num1 = int(input("Enter an integer: "))
# operator = input('Enter an operator from the list * / % + -: ')
# num2 = int(input('Enter another integer: '))

# operators = ['*', '/', '%', '+', '-']

# if operator not in operators:
#     print('That is not a valid operator.')
#     exit()

# if num2 == 0 and (operator == "/" or operator == '%'):
#     print('You cannot divide by zero.')
#     exit()

# if operator == '*':
#     print(f'{num1} * {num2} = {num1 * num2}')

# elif operator == '/':
#     print(f'{num1} / {num2} = {num1 / num2}')

# elif operator == '%':
#     print(f'{num1} % {num2} = {num1 % num2}')

# elif operator == '+':
#     print(f'{num1} + {num2} = {num1 + num2}')

# elif operator == '-':
#     print(f'{num1} - {num2} = {num1 - num2}')



# a = 10
# b = 5
# c = 3
# if a < b and b > c:
#     print("Banana")
# elif a < c or a < b:
#     print("Pizza")
# num = 2
# while num <= 10:
#     print(num, end=" ")
#     num += 2
# import turtle
# wn = turtle.Screen()
# t = turtle.Turtle()
# for _ in range(10):
#     t.forward(50)
#     t.right(36)
# wn.exitonclick()
# colors = ["red", "green", "blue"]
# for color in colors:
#     print(color, end=" - ") 
# sum = 0
# value = 0

# while value != -1:
#     value = int(input("Enter next number, -1 to quit: "))
#     if value != -1:
#         sum += value

# print("The sum of your numbers, other than -1, is", sum)

# print("This program will output the odd numbers 1, 3, ..., 19")
# for i in range(1, 21, 2):
#     print(i)

# sum = 0
# integer = 1

# while integer <= 10:
#     sum += integer
#     integer += 1

# print(f'The sum of the integers 1 to 10 is {sum}.')
for sum in range (1, 11):
    p