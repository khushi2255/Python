''' 
NOTE:-
       r+  read + overwrite  (ptr start) - no truncate
       w+  read + overwite               - truncate
       a+  read + append     (ptr  end)  - no truncate

'''


# f = open("sample.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()


f = open("sample.txt", "w+")
# f.write("abc")
print(f.read())
f.write("abc")
f.close()
