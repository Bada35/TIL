while 1:
  r = 'no'
  a = input()

  if a == '0':
    break
  if a == a[::-1]:
    r = 'yes'

  print(r)