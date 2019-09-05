a = int(input())
b = input()

reverse_b = reversed(b)
int_b = int(b)

resultSum = 0

for div_b in reverse_b:
    print(int(div_b)*a)

print(int_b * a)

