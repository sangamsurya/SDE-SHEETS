class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, n, arr):
        max_right = arr[n-1]
        leaders_list = []
        leaders_list.append(max_right)
        
        for i in range(n-2, -1, -1):
            if arr[i] >= max_right:
                leaders_list.append(arr[i])
                max_right = arr[i]
                    
        return leaders_list[::-1] 