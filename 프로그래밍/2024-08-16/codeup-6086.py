until = int(input())
sum = 0

for i in range(1, until + 1):
  sum += i
  if sum >= until:
    break

print(sum)
