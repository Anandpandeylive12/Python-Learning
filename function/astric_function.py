def summ_all(*args):
    print("Arguments received:", args)
    for i in args:
        print("Processing:", i)
    return sum(args)

print(summ_all(2, 3, 4, 5))  
print(summ_all(10, 20, 30,3,4,5,6,7,8,9))