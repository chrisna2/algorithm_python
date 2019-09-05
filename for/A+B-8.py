import sys

inp = int(input())
for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    case = i+1
    sum = a+b
    print("Case #"+str(case)+": "+str(a)+" + "+str(b)+" = "+str(sum))