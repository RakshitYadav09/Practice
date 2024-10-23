def SubArraySum(arr, n):
    temp, res = 0, 0
    
    for i in range(n):
        temp = 0
        for j in range(i, n):
            temp += arr[j]
            res += temp
    return res

# Driver code
arr = [1, 2, 3]
n = len(arr)
print("Sum:", SubArraySum(arr, n))