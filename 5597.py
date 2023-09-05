students = [i for i in range(1,31)]

for _ in range(28):    # 28 주의
    applied = int(input())
    students.remove(applied) 

print(min(students))
print(max(students))
