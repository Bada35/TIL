while 1:
  r = 'no'
  a = input()
  if a == '0':
    break
  if a == ''.join(reversed(a)):
    r = 'yes'
  print(r)