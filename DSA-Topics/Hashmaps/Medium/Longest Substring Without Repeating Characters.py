class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        return self.longestSubString(s)
    
    def longestSubString(self , stringValue : str) -> int:
        
        max_length = 0
        
        #Edge case
        if len(stringValue) == 0:
            return max_length
        
        left_ptr = 0
        right_ptr = 0
        
        memo = {}
        
        for right_ptr,chars in enumerate(stringValue):
            if chars in memo:
                if memo[chars]  >= left_ptr:
                    left_ptr = memo[chars] + 1
            memo[chars] = right_ptr            
            new_length = right_ptr - left_ptr + 1
            
            max_length = max(new_length , max_length)
            
        return max_length
        
        
        
