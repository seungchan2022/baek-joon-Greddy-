n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

result = []
for i in range(n):
    result.append(array[i] * (i + 1))

print(max(result))


"""
예를 들어 5개의 로프가 있다고 할 때 , 
이때 각 로프는 버틸 수 있는 최대 중량이 주어진다. 
array = [ 27, 23, 15, 11, 3 ] 
이렇게 있다면
- 로프가 1개라면 27 * 1 = 27 

-           2개            23 * 2 = 46

-           3개            15 * 3 = 45

-           4개            11 * 4 = 44

-           5개             3  * 5 = 15

-> 로프들을 이용해서(모든 로프를 사용하지 않아도 된다)
    들어올릴 수 있는 물체의 최대 중량을 구해내는 것이기 때문에 답은 46 이다! 
"""