#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order.

Results:
Runtime: 40 ms, faster than 94.45% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 43.26% of Python3 online submissions for Two Sum.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_number_idx, first_number in enumerate(nums):
            for second_number_idx, second_number in enumerate(nums):

                if first_number_idx == second_number_idx:
                    continue
                else:
                    sum_numbers = first_number + second_number

                if sum_numbers == target:
                    res = [first_number_idx, second_number_idx]
                    return res
