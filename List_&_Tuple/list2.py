marks = [89, 90, 78, 65, 27, 45, 77, 98]
print(marks)
# print(len(marks))
print(marks[:])
print(marks[1:8:3])


# List Comprehension
lst = [i for i in range(4)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
