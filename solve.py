n, m = map(int, input().split())  # 행 열

re = 0
for i in range(n):
    card = list(map(int, input().split()))
    mic = min(card)
    re = max(re, mic)

print(re)
