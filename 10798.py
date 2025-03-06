matrix = []

for _ in range(5):
    row = input()
    for i in range(len(row)):
        matrix.append(row[i])


result = ''.join(matrix)
print(result)


