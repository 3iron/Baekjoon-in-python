a = input().lower()
a_list = list(set(a))
cnt = []

for i in a_list:
    count = a.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2 : # 많이 있는게 여러개 있을 때
    print("?")
else:
    print(a_list[(cnt.index(max(cnt)))].upper())