def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[0:3]*n

def string_bits(str):
  return str[::2]

def array_count9(nums):
  z = 0
  for i in nums:
    if(i == 9):
      z += 1

  return z

def last2(str):
  l=0
  for i in range(len(str)-1):
    if(str[i:i+2] == str[-2:]):
      l+=1

  if (l > 0):
    return l-1
  return l


def string_splosion(str):
  s = ''
  for i in range(len(str)+1):
    s += str[:i]

  return s

def array_front9(nums):
  for i in range(len(nums)):
    if (i < 4 and nums[i] == 9):
      return True

  return False

def array123(nums):
  next = 1
  for i in range(len(nums)):
    if (nums[i] != next):
      next = 1

    if (nums[i] == next):
      next += 1
      if (next == 4):
        return True

  return False
