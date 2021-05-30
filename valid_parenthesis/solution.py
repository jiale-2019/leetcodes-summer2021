# Source: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def is_match(self, i:int, s_list:list) -> bool:
        
        if s_list[i] == '(' and s_list[i+1] == ')':
            return True
        
        if s_list[i] == '[' and s_list[i+1] == ']':
            return True
        
        if s_list[i] == '{' and s_list[i+1] == '}':
            return True
        
        return False
    
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        i = 0
        
        while i < len(s_list)-1:
            
            if self.is_match(i,s_list):
                s_list.pop(i)
                s_list.pop(i)
                i = max(0, i-1)
                
            else:
                i +=1
        
        if s_list:
            return False
        return True