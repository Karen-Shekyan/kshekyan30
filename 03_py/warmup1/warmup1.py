def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return not (a_smile ^ b_smile)

def sum_double(a, b):
  if (a == b):
    return 4 * a
  else:
    return a + b

def diff21(n):
  if (n > 21):
    return 2* (n - 21)
  else:
    return 21 - n

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10

def pos_neg(a, b, negative):
  return not negative and ((a > 0) ^ (b > 0)) or negative and (a < 0 and b < 0)

def not_string(str):
  if (str[0:3] == "not"):
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  return str if len(str) == 1 else str[-1:] + str[1:len(str)-1] + str[:1]

def front3(str):
  if(len(str) < 3):
    return str + str + str
  return str[0:3] + str[0:3]+str[0:3]

# print(not_string("hi")    )
