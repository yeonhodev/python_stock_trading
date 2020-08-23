crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics', 'CRSP': 'CRISPR Therapeutics'}
# % 기호 방식
for x in crispr:
  print('%s : %s' % (x, crispr[x])) # old school format

# {} 기호 방식
for x in crispr:
  print('{} : {}'.format(x, crispr[x])) # new school format

# f-string 방식
for x in crispr:
  print(f'{x} : {crispr[x]}') # brand new school format
  