class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make list 
        s_list = list(s)
        t_list = list(t)

        for char in s_list:
            if char in t_list:
                t_list.remove(char)
            else:
                return False

        return True if not t_list else False
        
