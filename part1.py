def parity_split(nums):
    nums_even = [n for n in nums if n % 2 == 0]
    nums_odd = [n for n in nums if n % 2 != 0]
    return nums_even, nums_odd


assert parity_split([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])
assert parity_split([1, 1]) == ([], [1, 1])
assert parity_split([0]) == ([0], [])
