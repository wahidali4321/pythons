def count_up_to(n):
  count = 0
  while count <= n:
    yield count
    count += 2

for num in count_up_to(20):
  print(num)