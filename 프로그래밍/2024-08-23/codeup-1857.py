def get_cases(n: int, r: int) -> int:
  if r == 0 or n == r:
    return 1
  return get_cases(n - 1, r - 1) + get_cases(n - 1, r) if n >= r else 0

def main():
  n, r = map(int, input().split())
  print(get_cases(n, r))

if __name__ == '__main__':
  main()
