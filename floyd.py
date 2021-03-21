size = int(input("Enter the range:  "))
print("FLOYD'S TRIANGLE with numbers: \n")
k = 1

for i in range(1, size + 1):
    for j in range(1, i + 1):
        print(k, end=" ")
        k = k + 1
    print()
print("\n")
