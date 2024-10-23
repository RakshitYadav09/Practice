def findDistinct(arr):
    res = []
    
    # Nested loops
    # for i in range (len(arr)):
        
    #     j=0
    #     while j<i: 
    #         if arr[i]==arr[j]:
    #             break
    #         j += 1
    #     if i==j:
    #         res.append(arr[i])
    # return res
    
    # Using sorting
    n=len(arr)
    arr.sort()
    
    for i in range(n):
        if i == 0 or arr[i] != arr[i-1]:
            res.append(arr[i])
            
    return res


        
        
    