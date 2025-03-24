word = input().upper()  # 대소문자 구분 없이 처리
letter_count = {}

# 각 알파벳의 개수 세기
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

# 최다 빈도 계산
max_count = max(letter_count.values())
max_letters = [k for k, v in letter_count.items() if v == max_count]

# 결과 출력
if len(max_letters) > 1:
    print("?")
else:
    print(max_letters[0])
