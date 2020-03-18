def double_char(str):
  result = ""
  for i in range(len(str)):
    result += str[i] + str[i]
  return result