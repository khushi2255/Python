def func1():
    try:
        list1 = [1, 5, 7, 9]
        i = int(input("Enter the index: "))
        print(list1[i])
        return 1
    except:
        print("Some error occured")
        return 0
    
    finally:
        print("I am always executed")


x = func1()
print(x)
