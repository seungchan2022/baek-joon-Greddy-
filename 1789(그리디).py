s = int(input())

n = 1
while n * (n + 1) / 2 <= s:
    n += 1

print(n - 1)

"""
s = int(input())
total = 0   # 자연수들의 합
count = 0   # 늘어나는 자연수

while True:
    count += 1      # 자연수 1씩 증가
    total += count
    if total > s:
        break
"""


"""                
서로다른 n개의 자연수의 합이 s일때 n의 최댓값을 구하는 알고리즘이다.
최댓값을 구하는 문제이므로 1부터 차례대로 더해 s보다 커지게 되면 그 수에서 1을 빼면 된다.
n * (n + 1) / 2 는 1부터 n까지의 합의 공식이다(등차 수열)
"""
