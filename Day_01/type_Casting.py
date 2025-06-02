# Type Casting :
# (i) Implicit - compiler type caste krta h (Automatically)
# (ii) Explicit- user khud se type caste krta h (Manually)

num1 = input("Enter first number: ")  # by defualt it is string type
num2 = input("Enter second number: ")
print(num1 + num2)

# type Casting

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))
print(num1 + num2)

# example 2

num1 = 20
num2 = 20.5
print(
    num1 + num2
)  # smaller value ko large value mein convert krte h. like, convert (int) into (float)
print(num1 * num2)
