#  --- DICTIONARY METHODS ---

# (i)  myDict.keys() -> returns all keys.
# (ii)  myDict.values() -> returns all values
# (iii) myDict.items()  -> returns all (key, val) pair as tuples
# (iv) myDict.get("key") -> returns the key accroding to value
# (v) myDict.update(newDict) -> inserts the specified items to the dictionary.


student = {
    "name": "Arav Sharma",
    "subjects": {
        "chemistry": 89,
        "physics": 98,
        "maths": 87,
    },
}
# print(student.keys())
print(list(student.keys()))  # typecast into list

print(list(student.values()))


# print(list(student.items()))
pairs = list(student.items())
print(pairs[1] )

print(list(student.get("name")))


# student.update({"city" : "Siwan"})
new_dic = {"city": "Siwan", "age": 14}
student.update(new_dic)
print(student)
