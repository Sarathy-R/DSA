class Solution:

    def longestKSubstr(self, s, k):
        # code here
        max_length = 0
        
        if len(s) == 0:
            return max_length
        
        
        left_ptr = 0
        memo = {}
        
        for right_ptr , chars in enumerate(s):
            
            if chars in memo:
                memo[chars] = memo[chars] + 1
            else:
                memo[chars] = 1
                
            # If condition is valid
            if len(memo) == k:
                new_length = right_ptr - left_ptr + 1
                max_length = max(new_length , max_length)
            
            # If condition fails
            if len(memo) > k:
              
                # Reduces the len(memo) to k again
                while len(memo) != k:
                    present_char = s[left_ptr:left_ptr+1]
                    if present_char in memo:
                        memo[present_char] = memo[present_char] - 1
                        if memo[present_char] == 0:
                            del memo[present_char]
                    
                    left_ptr += 1
        return -1 if max_length == 0 else max_length
