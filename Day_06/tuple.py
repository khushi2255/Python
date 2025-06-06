# Tuples-> A built-in data type that lets us create immutable sequence of values.

tup = (87, 56, 57, 35, 46)
print(tup[0])
print(tup[1])
# tup[0]=35 -> this will throw error
print(tup[1:3])  # tuple slicing


tup1=("khushi",) # we put the comma at the last to give the (tuple) type.
print(tup1)
print(type(tup1))

tup2=(56,)
print(tup2)
print(tup2[1:3])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")