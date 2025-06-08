marks = [12, 89, 67, 56, 45, 77, 60]

# index = 0
# for mark in marks:
#     print(mark)

#     if index == 3:
#         print("Khushi, awesome!")
#     index += 1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print("khushi, Awesome!")
