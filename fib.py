while True:
    try:
        length = int(input("Give the length of the fibonacci series (must be positive): "))
        start = int(input("Give the starting number: "))
        break
    except:
        print("Give a valid number.")

fibo = [0,1]
    
if start < 2:
    for i in range(length-1):
        fibo.append(fibo[-2] + fibo[-1])
else:
    while fibo[-1] < start:
        fibo.append(fibo[-2] + fibo[-1])
    fibo.append(fibo[-2] + fibo[-1])
    fibo = fibo[-3:]
    for i in range(length-2):
        fibo.append(fibo[-2] + fibo[-1])


fibo = fibo[1:] # Cut the first one
fibo = fibo[:length] # Crop to length
print(fibo)

file = open("fibonacciresult.txt", "w+")

for n in fibo:
    file.write(str(n) + "\n")

file.close()
