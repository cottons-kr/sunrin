def find_missing_number(numbers: list, count: int) -> int:
  total = (count + 1) * count // 2
  return total - sum(numbers)

def main():
  numbers: list[int] = []
  count = int(input())

  for _ in range(0, count - 1):
    numbers.append(int(input()))

  print(find_missing_number(numbers, count))

if __name__ == '__main__':
  main()
