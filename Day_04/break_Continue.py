# Break: to break the loop
# Continue: to skip the iteration.


# Break
for i in range(12):
    if i == 10:
        break
    print("5 x", i + 1, "=", 5 * (i + 1))



# Continue  
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("6 x", i + 1, "=", 6 * (i + 1))
