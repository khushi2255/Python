"""
IMP NOTE :  SET -> MUTABLE   ,  SET ELEMENTs -> Immutable.

(i)  set.add(el) --> adds an element
(ii) set.remove(el) --> remove the element
(iii) set.clear()  --> empties the set
(iv) set.pop()  --> remove a random value


"""

collection = set()
collection.add(77)
collection.add(23)
collection.add(70)
collection.add("Khushi")
# collection.add(1, 2, 3, 4)
print(collection)
print(len(collection))


collection.remove(23)
print(collection)


collection.pop()
print(collection)


collection.clear()
print(collection)