#sliding-window
#https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s) 
        
        left, right = 0,0 
        longest = 0 
        dict1 = collections.defaultdict(int) 

        while left < n and right < n:
            lr = s[right]
            if(len(set(list(dict1.keys()) + [lr])) <= k):
                if lr not in dict1: dict1[lr] = 1
                else: dict1[lr] += 1
                right += 1 
                longest = max(longest, right - left)

            else:
                ll = s[left]
                dict1[ll] -= 1
                if dict1[ll] == 0:
                    dict1.pop(ll, None)
                left += 1  
        return longest
                
                
        