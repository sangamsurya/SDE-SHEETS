class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        d1 = {}
        d2 = {}
        
        for i in arr1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
                
        for i in arr2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
    
        return d1==d2
            