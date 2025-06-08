# n = input("Enter the number: ")
# print(f"Multiplication table of {n} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(n)} x {i} = {int(n)*i}")
# except:
#     print("Invalid input")

# print("Some imp lines of code")
# print("End of program")


try:
    num = int(input("Enter an integer: "))
    a = [5, 9]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error")
