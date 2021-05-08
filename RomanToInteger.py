#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Results:
Runtime: 44 ms, faster than 78.80% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.1 MB, less than 83.30% of Python3 online submissions for Roman to Integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        res = []
        list_s = list(s)
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        found_bigger = False

        for idx, roman_number in enumerate(list_s):
            if found_bigger:
                found_bigger = False
                continue

            number = roman_numbers.get(roman_number)

            if idx != len(list_s) - 1:
                next_number = roman_numbers.get(list_s[idx + 1])
            else:
                next_number = number

            if next_number > number:
                found_bigger = True
                res.append(next_number - number)
            else:
                res.append(number)

        return sum(res)
