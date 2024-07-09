n = int(input("Enter the number of tuples: "))
tuples = []
for i in range(n):
    s = input("Enter the string: ")
    tuples.append((s, len(s)))

tuples.sort(key=lambda x: x[1])
print(tuples)