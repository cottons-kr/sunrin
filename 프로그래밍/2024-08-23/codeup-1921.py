def decimal_to_custom_count_system(n: int, base: int) -> None:
  if n == 0:
    return
  decimal_to_custom_count_system(n // base, base)

  if n % base < 10:
    print(n % base, end='')
  else:
    print(chr(n % base + 55), end='')

def main():
  n, base = map(int, input().split())
  if n == 0:
    print(0)
    return
  decimal_to_custom_count_system(n, base)
  print()

if __name__ == '__main__':
  main()
