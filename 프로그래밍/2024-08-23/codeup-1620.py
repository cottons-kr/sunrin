def sum_each_number(number: int) -> int:
  return sum(map(int, str(number)))

def main():
  input_number = int(input())
  while input_number >= 10:
    input_number = sum_each_number(input_number)
  print(input_number)

if __name__ == '__main__':
  main()
