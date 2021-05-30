# Source: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        diction_val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        s_list = list(s)
        
        total_val = 0
        i = 0
        
        while i < len(s_list)-1 :
            
            pair_val = self.check_pair(i,s_list)
            
            if pair_val:
                total_val += pair_val
                s_list.pop(0)
                s_list.pop(0)
            
            else:
                total_val += diction_val[s_list[i]]
                s_list.pop(0)
                
        if s_list:
            total_val += diction_val[s_list[0]]
        
        return total_val
    
    def check_pair(self, i: int, s_list: list) -> int:
        
        letter_pair = s_list[i] + s_list[i+1]
        
        if letter_pair == 'IV':
            return 4
        
        elif letter_pair == 'IX':
            return 9
        
        elif letter_pair == 'XL':
            return 40
        
        elif letter_pair == 'XC':
            return 90
        
        elif letter_pair == 'CD':
            return 400
        
        elif letter_pair == 'CM':
            return 900
        
        else:
            return 0