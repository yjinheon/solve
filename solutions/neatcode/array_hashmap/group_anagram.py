from typing import List
from collections import defaultdict

class Solution:
    def group_anagram(self,strs: List[str])->List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:

            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())

