finst_num = int(input())

check_val = finst_num
cnt = 0
while True:
    second_num = finst_num % 10
    finst_num = int(finst_num/10)
    rslt_num = finst_num + second_num
    finst_num = (second_num*10) + rslt_num%10

    if check_val == finst_num:
        cnt += 1
        break;
    else:
        cnt += 1


print(cnt)

