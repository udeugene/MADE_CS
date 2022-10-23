def parity_split(nums):
    nums_even = [n for n in nums if n % 2 == 0]
    nums_odd = [n for n in nums if n % 2 != 0]
    return nums_even, nums_odd
