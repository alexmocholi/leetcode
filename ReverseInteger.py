#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/reverse-integer/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Results:
Runtime: 32 ms, faster than 64.57% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 10.93% of Python3 online submissions for Reverse Integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = int(str(abs(x))[::-1]) * -1
        elif x == 0:
            return 0
        else:
            res = int(str(x)[::-1])

        if res.bit_length() > 31:
            return 0
        else:
            return res

