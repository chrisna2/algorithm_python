H, M = map(int, input().split())

check = M - 45

if -45 <= check < 0:
    H = H - 1
    if H == -1:
        H = 23
    M = 60 + check
else:
    M = check

print(str(H)+" "+str(M))
