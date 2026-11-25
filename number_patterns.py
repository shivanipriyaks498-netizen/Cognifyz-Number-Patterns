
print("================================")
print("       NUMBER PATTERNS")
print("================================")

rows = int(input("Enter the number of rows: "))

print("\n1. Increasing Number Pattern")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n2. Number Pyramid")

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print("\nPattern generation completed!")
