def find_hcf(a,b):
    hcf = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           hcf = i
    return hcf


first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

print('hcf = ', find_hcf(first, second))

lcm = first * second /find_hcf(first, second)
print('LCM =' , lcm)