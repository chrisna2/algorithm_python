N = int(input())
list_num = list(map(int, input().split()))

list_num.sort()

print(str(list_num[0])+" "+str(list_num[-1]))