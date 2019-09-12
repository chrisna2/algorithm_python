"""
문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.

"""

if __name__ == '__main__':

    fraction_number = int(input())
    chasu = 1
    step = 1
    step_val = 1
    # 각 분자 분모의 합이 step :
    # step 의 값이 제일 먼저 나오는 순서 step_val :
    # step_val의 차수는 1씩 늘어남 :
    # 지그재그 : step : 짝수이면 분모가 늘어나고 : 홀수이면 분자가 늘어남
    while True:
        step += 1
        step_val = step_val + chasu
        if fraction_number < step_val:
            step_val = step_val - chasu
            break
        chasu += 1

    k = fraction_number - step_val

    if step % 2 == 0:
        print(str(step - k - 1) + "/" + str(k + 1))
    else:
        print(str(k + 1) + "/" + str(step - k - 1))

