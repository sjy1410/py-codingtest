n, target = map(int, input().split())
arr = list(map(int, input().split()))


def f(n, target):
    for i in arr:
        if i == target:
            return arr.index(target)+1
    return '원소가 존재하지 않습니다.'

print(f(n,target))