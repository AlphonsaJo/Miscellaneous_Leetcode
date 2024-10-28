class Solution(object):
    def isSubsequence(self, s, t):
 
        s_pointer = 0

       
        for char in t:
      
            if s_pointer < len(s) and s[s_pointer] == char:
                s_pointer += 1
                
           
            if s_pointer == len(s):
                return True

        
        return s_pointer == len(s)


      



        