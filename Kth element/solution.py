
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i = 0
        j = 0
        pos = 0
        
        res = 0
        
        while (pos != k):
            if j == len(arr2):
                d = i + (k-pos)
                res = arr1[d-1]
                break
                
            if i == len(arr1):
                d = j + (k-pos)
                res = arr2[d-1]
                break
            
            if arr1[i] >= arr2[j]:
                res = arr2[j]
                j+=1
                
                    
            elif arr2[j] > arr1[i]:
                res = arr1[i]
                i+=1
                
                    
            pos+=1
            
            
        return res
            
            
            