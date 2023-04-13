def solution(a):
    c = [0] * (max(a)+1)

    for i in a:
        c[i] += 1

    m = 0
    for i in c:
        if i == max(c):
            m += 1

    if m > 1:
        return -1
    else:
        return c.index(max(c))


a = list(map(int, input().split()))
print(solution(a))
