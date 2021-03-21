def fib(num):
    if num <= 1:
        return num
    else:
        return(fib(num-1)+fib(num-2))
    for i in range (num):
        print(fib(i))

    