# DAY 25/08/2025

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""
POSSIBLE SOLUTIONS:
Horizontal scanning (I used this)
Intuition: Assume the first string is the common prefix, then compare it with the others. For each string, if it doesn't start with the current prefix, reduce the prefix by one character and check again.
- Time complexity: O(S), where S is the sum of all characters in all strings.
- Space complexity: O(1), since we are using only a constant amount of extra space.

Vertical scanning
Intuition: Compare characters of the strings one by one. For each position, check if all strings have the same character. If not, return the prefix found so far.
- Time complexity: O(S), same.
- Space complexity: O(1).

Divide and Conquer
Intuition: Split the array into two halves, find the longest common prefix in each half, and then merge the results.
- Time complexity: O(S).
- Space complexity: O(log N), because we are using recursion, where N is the number of strings.

Trie
Intuition: Build a trie (prefix tree) from the strings, the prefix will be the path to the root that have more than one child.
- Time complexity: O(S), where S is the sum of all characters in all strings.
- Space complexity: O(N * M), where N is the number of strings and M is the length of the longest string.

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for indx in strs:
            while len(first) > 0:
                if not indx.startswith(first):
                    first = first[:-1]
                else:
                    break
            if len(first) == 0:
                return ""
        return first