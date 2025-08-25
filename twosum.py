"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

"""
BEST SOLUTION
Intuition: Store numbers already seen in a HashMap to quickly check if the complement `target - nums[i]` has already appeared.
- Time complexity: O(n)
- Space complexity: O(n)

OTHER BAD SOLUTIONS
Brute force: Iterate over the array and check if any pair combination sums equal to `target`
Sorting + two pointers: Sort the array and use two pointers to find the pair that sums equal to `target`
"""

class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for ind, x in enumerate(nums):
            if map.get(x) is not None:
                return [map.get(x), ind]
            map[target-x] = ind