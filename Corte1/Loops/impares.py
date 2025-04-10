
times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

if times == 0:
    print("Don't do anything")
else:
    for i in range(1,times+1):
        print("i = ", i)