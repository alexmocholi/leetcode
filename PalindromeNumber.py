#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/palindrome-number/
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Follow up: Could you solve it without converting the integer to a string?

Results:
Runtime: 76 ms, faster than 16.46% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.3 MB, less than 48.34% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reversed = 0
        last_quotient = x

        if x < 0:
            return False

        while True:
            quotient = int(last_quotient / 10)
            number = last_quotient - quotient * 10
            x_reversed = x_reversed * 10 + number
            last_quotient = quotient

            if last_quotient == 0:
                break

        return x_reversed == x
