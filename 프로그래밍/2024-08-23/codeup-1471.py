'''
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
3 4 9
2 5 8
1 6 7

입력이 5인 경우는 다음과 같이 출력한다.
5 6 15 16 25
4 7 14 17 24
3 8 13 18 23
2 9 12 19 22
1 10 11 20 21

입력이 n인 경우의 2차원 배열을 출력해보자.
'''

def main():
  n = int(input())
  for i in range(n):
    for j in range(n):
      print(n * (n - j) - i, end=' ')
    print()

if __name__ == '__main__':
  main()
