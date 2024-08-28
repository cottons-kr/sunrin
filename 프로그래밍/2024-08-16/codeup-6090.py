# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)
a, m, d, n = map(int, input().split())
array = [a]

for i in range(n - 1):
  array.append(array[i] * m + d)

print(array[-1])
