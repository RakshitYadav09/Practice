def ExceptSelf(nums, n):
    c = 0
    prod = 1
    res =[0]*n
    
    for num in nums:
        if num == 0:
            c += 1
        else:
            prod *= num
    
    for i in range(n):
        if c > 1:
            res[i]=0
        elif c==1:
            if nums[i]==0:
                res[i]=prod
            else:
                res[i]=0
        else:
            res[i]=prod//nums[i]
            
    return res