class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self, arr):
        
        if len(arr) == 1:
            return 1
        elif len(arr) == 2:
            if arr[0] == 0:
                return 2 
            if arr[1] == 0:
                return 1 
                
                
            return -1 
        i = 0
        j = len(arr) - 1
        left_sum = arr[i]
        right_sum = arr[j]
        
        while i < j:
            if left_sum < right_sum:
                i += 1
                left_sum += arr[i]
            elif right_sum < left_sum:
                j -= 1
                right_sum += arr[j]
            else: 
                if i + 1 == j - 1:
                    return i + 2 
                i += 1
                left_sum += arr[i]
                j -= 1
                right_sum += arr[j]
    
        return -1 


                
            