List1 = [3, 10, 6, "khushi", True]
print(List1)
print(type(List1))

# print(List1[0])
# print(List1[1])
# print(List1[2])
# print(List1[3])
# print(List1[4])

print(List1[-3])  # negative idx
print(List1[len(List1) - 3])  # positive idx
print(List1[5 - 3])
print(List1[2])

if "khushi" in List1:
    print("Yes")
else:
    print("No")


#same thing applies for string as well!
if "shi" in "khushi":
    print("Yes")
