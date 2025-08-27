"""
DAY 26/08/2025
Given an integer x, return true if x is a palindrome, and false otherwise.

MY SOLUTION
Intuition:Build an array of digits, extracting the last digit in number (x % 10), and check if it reads the same forwards and backwards.
- Time complexity: O(n), where n is the number of digits in x
- Space complexity: O(n), for the digits array

OTHERS SOLUTION
Converting to String (This was my first approach)
Intuition: Convert the integer to a string and check if the string is a palindrome.

Reverse only half of the number (More performatic and elegant)
Intuition: Reverse the last half of the digits and compare it with the first half. This avoids the need for extra space.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False     
        
        x2 = x
        digits = []
        while x2 > 0: 
            digits.append(x2 % 10) 
            x2 //= 10 
        
        return digits == digits[::-1]