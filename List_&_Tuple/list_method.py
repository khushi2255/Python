# list=[2, 1, 3]
# (i) list.append(4) -> adds one element at the end [2, 1, 3, 4]
# (ii) list.sort()  -> sorts in ascending order [1, 2, 3]
# (iii) list.sort(reverse=True)  -> sorts in descending order [3, 2, 1]
# (iv) list.reverse()  -> reverses list  [3, 1, 2]
# (v) list.insert(idx,el) 
# (vi) list.remove(1)  -> remove first occurence of element [2, 3, 1]
# (vii)  list.pop(idx)  -> removes element at idx
# (viii) del  -> The del keyword also removes the specified index.

list1 = [2, 1, 3]
list1.append(4)  # add 4 at the end.
print(list1)
list1.sort()  # sort the element in the ascending order.
print(list1)
list1.pop(1)
print(list1)


list2 = ["a", "b", "c", "d"]
list2.sort(reverse=True)  # sort the element in decsending order.
print(list2)
list2.insert(3, "k")
print(list2)
list2.remove('a')
print(list2)
