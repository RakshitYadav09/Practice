def findDistinct(arr):
    res = []
    
    for i in range (len(arr)):
        
        j=0
        while j<i: 
            if arr[i]==arr[j]:
                break
            j += 1
        if i==j:
            res.append(arr[i])
    return res

if __name__ == "__main__":
    arr = [12, 10, 9, 45, 2, 10, 12, 45, 11]
    res = findDistinct(arr)
    for val in res:
        print(val, end=" ")
        
        
    