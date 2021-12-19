#!/usr/bin/env python
"""
file:        3-longest-substring-without-repeating-characters.py
author:      jinxin
email:       jinxin.ashin@outlook.com
description: Give a string `s`, find the length of the longest substring without repeating characters. Note that the
answer must be a substring, not a subsequence.
"""


class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        """my solution"""
        l = len(s)
        if l == 0:
            return 0
        if l == 1:
            return 1
        dp = [1] * l
        for i in range(1, l):
            pre_dp = dp[i - 1]
            if (len(set(s[i - pre_dp : i])) == pre_dp) and (
                s[-1] not in s[i - pre_dp : i]
            ):
                dp[i] = pre_dp + 1
            else:
                dp[i] = pre_dp
        return dp[-1]

    def solution_by_sliding_window(self, s: str) -> int:
        slen = len(s)
        if slen == 0:
            return 0
        i = j = 0
        charlist = set()
        maxlen = 0
        while i < slen and j < slen:
            if s[j] not in charlist:
                charlist.add(s[j])
                maxlen = max(maxlen, j - i + 1)
                j += 1
            else:
                charlist.remove(s[i])
                i += 1
        return maxlen

    def solution_by_best_dp(self, s: str) -> int:
        slen = len(s)
        if slen == 0:
            return 0
        chardict = dict()
        maxlen = 0
        last_start = -1
        for i in range(slen):
            last_start = max(last_start, chardict.get(s[i], -1))
            maxlen = max(maxlen, i - last_start)
            chardict[s[i]] = i
        return maxlen


if __name__ == "__main__":
    solution = Solution()

    s = "swese"
    l = solution.lengthofLongestSubstring(s=s)
    print("max length of non-repeating substring in '%s' is %d." % (s, l))
