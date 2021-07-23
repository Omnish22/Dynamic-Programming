# result = []
# def howSum(targetSum,arr):
#     if targetSum == 0:
#         return []
#     elif targetSum<0:
#         return False
    
#     for i in arr:
#         d = targetSum - i 
#         if howSum(d,arr) != False:
#             ans = howSum(d,arr)
#             ans.append(i)
#             return ans

#     return False 


memo = {}
def howSum(target,arr):
    if target in memo:
        return memo[target]
    elif target==0:
        return []
    elif target<0:
        return False
    
    for num in arr:
        d = target - num
        # print(f"num:{num} node:{d}")
        ans = howSum(d,arr)
        memo[d]=ans
        # print("\n")
        if ans !=False:
            ans.append(num)
            return ans 
    return False

print(howSum(300,[7,14,1]))

