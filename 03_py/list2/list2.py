def count_evens(nums):
  evens = 0
  for i in range(len(nums)):
    if (nums[i] % 2 == 0):
      evens += 1

  return evens

def big_diff(nums):
  small = nums[0]
  big = nums[0]
  for i in range(len(nums)):
    small = min(nums[i], small)
    big = max(nums[i], big)

  return big - small
