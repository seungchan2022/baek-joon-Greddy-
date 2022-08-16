n = input()

# 가장 큰수를 만들기 위해 큰 숫자를 앞으로 옮김
n = sorted(n, reverse=True)
sum = 0     # 각 자릿수 더한 값(3의 배수를 판단하기 위해 변수 설정)

if '0' not in n:
    print('-1')
else:
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 3 != 0:
        print('-1')
    else:
        print(''.join(n))


# 30의 배수는 3의 배수이면서 일의 자리가 0인 수이다.