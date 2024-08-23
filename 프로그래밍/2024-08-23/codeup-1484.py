def print_snail(width: int, height: int) -> None:
  snail = [[0] * width for _ in range(height)]
  x, y = 0, 0
  dx, dy = 0, 1
  for i in range(1, width * height + 1):
    snail[x][y] = i
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= height or ny < 0 or ny >= width or snail[nx][ny] != 0:
      dx, dy = dy, -dx
      nx, ny = x + dx, y + dy
    x, y = nx, ny
  for i in range(height):
    for j in range(width):
      print(snail[i][j], end=' ')
    print()

def main():
  n, m = map(int, input().split())
  print_snail(m, n)

if __name__ == '__main__':
  main()
