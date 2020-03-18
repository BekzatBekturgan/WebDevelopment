def count_hi(str):
  cnt = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      cnt +=1
  return sum