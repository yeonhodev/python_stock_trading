i = 1
while i < 7:
  print(i)
  i += 2

print()

j = 0
while j >= 0:
  j += 1
  if (j % 2) == 0:
    continue
  if j > 5:
    break
  print(j)
else:
  print('Condition is False.')