N, X = map(int, input().split())
list_num = list(map(int, input().split()))

rslt_num = []

for i in list_num:
    if i < X:
        rslt_num.append(i)

for r in rslt_num:
    print(r, end=" ")