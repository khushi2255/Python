f = open("Demo.txt", "r")

# data = f.read()
# print(data)

line1 = f.readline()  # reads one line at a time
print(line1)

line2 = f.readline()
print(line2)

f.close()
