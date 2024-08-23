def main():
  h, w = map(int, input().split())
  n = int(input())
  board = [[0] * w for _ in range(h)]

  for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1

    for i in range(l):
      if d == 0:
        board[x][y + i] = 1
      else:
        board[x + i][y] = 1

  for row in board:
    print(' '.join(map(str, row)))

if __name__ == '__main__':
  main()
