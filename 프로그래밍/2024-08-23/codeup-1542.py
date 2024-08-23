def is_prime(target: int) -> bool:
  if target == 1:
    return False
  for i in range(2, target):
    if target % i == 0:
      return False
  return True

def main():
  number = int(input())
  print('prime' if is_prime(number) else 'composite')

if __name__ == '__main__':
  main()
