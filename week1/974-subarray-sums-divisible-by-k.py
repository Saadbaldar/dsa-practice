# LeetCode 974. Subarray Sums Divisible by K
# Week 1 test, 25 Nov 2026 — solved

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            rem = ((prefix_sum % k) + k) % k  # universal normalization

            if rem in rem_count:
                count += rem_count[rem]

            rem_count[rem] = rem_count.get(rem, 0) + 1

        return count
