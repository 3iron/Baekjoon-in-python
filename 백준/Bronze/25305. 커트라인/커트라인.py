# n : 학생 인원
# k : 커트라인
n, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[k-1])