# def bestSum(target,arr):
#     if target==0:
#         return []
#     elif target<0:
#         return None
    
#     shortestCombination = None
#     # print(f"NODE:{target}")
#     for num in arr:
#         # print(f"num:-{num}")
#         d = target - num 
#         ans = bestSum(d,arr)
#         # print(f"Target:{d} ans:{ans}")
#         if ans!=None:
#             ans.append(num)
#             # print(f"ans:{ans} num:{num}")
#             if (shortestCombination==None) or len(shortestCombination)>len(ans):
#                 shortestCombination = ans
#                 # print("shortest combo:",shortestCombination)

#     # print("\n")
#     return shortestCombination



memo={}
def bestSum(targetSum, numbers):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        ans = bestSum(remainder, numbers)

        if ans is not None:
            combination = ans + [num]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination.copy()

    if shortestCombination!=None:
        memo[targetSum] = shortestCombination.copy()
    else:
        memo[targetSum] = None
    return shortestCombination


# print(bestSum(7,[7,5,3,4]))
# print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
# print(bestSum(100,[1,2,5,25]))
