def main():
  n = int(input())
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print(i + n * (j - 1), end=' ')
    print()
  
if __name__ == '__main__':
  main()
