
n,m,k = map(int,input().split())

# 배열크기 n , 더해지는 횟수 m, k번 초과해서 대해질 수 없다
a = list(map(int, input().split()))
a.sort()
first = a.pop()
second = a.pop()
flag = True
res = 0
idx = 0
while m > 0:
    for i in range(k):
        if m == 0:
            break
        else:
            res += first
            m -= 1

    if m == 0:
        break
    else:
        res += second
        m -= 1

print(res)