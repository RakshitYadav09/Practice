def maxWater(arr):
    left = 1
    right = len(arr) - 2
    
    lmax = arr[left-1]
    rmax = arr[right+1]
    res = 0 
    
    while left<=right:
        if rmax <= lmax:
            res += max(0, rmax-arr[right])
            rmax = max(rmax, arr[right])
            right -=1
        else:
            res += max(0, lmax-arr[left])
            lmax = max(lmax, arr[left])
            left +=1
    
    return res
