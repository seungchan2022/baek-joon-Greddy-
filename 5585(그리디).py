coin = [500, 100, 50, 10, 5, 1]

n = 1000 - int(input())
result = 0

for i in coin:
    result += n // i
    n = n % i

print(result)

# 이코테 예제) 거스름돈과 유사