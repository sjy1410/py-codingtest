n = input()
row = int(n[1])  # 행
column = ord(n[0])-96  # 열

# 나이트의 이동방식
steps = [[1, 2], [1, -2], [2, 1],
         [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

# 이동 가능한 경우의 수 카운트
cnt = 0
for i in steps:
    nx = row+i[0]
    ny = column+i[1]
    if nx <= 8 and nx >= 1 and ny >= 1 and ny <= 8:
        cnt += 1

print(cnt)
