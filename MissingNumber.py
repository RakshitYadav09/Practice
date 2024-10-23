def missingNumber(n, arr):
    sum_arr=sum(arr)
    
    expected_sum=(n*(n+1))//2
    
    return expected_sum-sum_arr

