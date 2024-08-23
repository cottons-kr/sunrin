def decimal_to_binary(n):
  if n == 0:
    return
  decimal_to_binary(n // 2)
  print(n % 2, end='')

def main():
  n = int(input())
  if n == 0:
    print(0)
    return
  decimal_to_binary(n)
  print()

if __name__ == '__main__':
  main()
