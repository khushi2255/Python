"""
Create a new file "practice.txt
 using python. Add the following data in it:

    Hi everyone
    We are learning File I/O
    using Python.
    I like programming in Python.

"""

with open("practice.txt", "w") as f:
    f.write("Hi everyone \nWe are learning File I/O\n")
    f.write("using Python.\nI like programming in Python.")
