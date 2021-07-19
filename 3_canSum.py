def canSum(n,arr):
    if n==0:
        return True 
    elif n<0:
        return False 

    
    for i in arr:
        d = n-i
        if (canSum(d,arr)==True):
            return True 
    return False    



print(canSum(7,[1,5]))  # true 
# print(canSum(300,[7,14]))



memo = {}
def memoCanSum(targeSum,arr):
    if targeSum in memo:
        return memo[targeSum]
    elif targeSum == 0:
        return True 
    elif targeSum<0:
        return False 

    for i in arr:
        d = targeSum-i 
        if memoCanSum(d,arr)==True:
            memo[d] = True 
            return True 
    
    memo[d] = False 
    return False 


print(memoCanSum(300,[7,14]))