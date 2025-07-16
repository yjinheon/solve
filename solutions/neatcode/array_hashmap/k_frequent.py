from collections import Counter
from typing import List


class Solution:

    def top_k_frequent(self,nums: List[int], k: int)-> List[int]:
        counter = Counter(nums)
        most_common = counter.most_common(k)
        result = []

        for num , count in most_common:
            result.append(num)

        return result




