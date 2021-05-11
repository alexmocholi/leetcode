#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

(Solution based on comment by pye)
Results:
Runtime: 28 ms, faster than 92.19% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.5 MB.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if len(strs) == 0:
            return prefix

        for idx in range(len(min(strs))):
            char = strs[0][idx]

            if all(word[idx] == char for word in strs):
                prefix += char
            else:
                break

        return prefix
