memo = {}
def bestSum(target,arr):
    if target==0:
        return []
    elif target<0:
        return None
    
    shortestCombination = None
    # print(f"NODE:{target}")
    for num in arr:
        # print(f"num:-{num}")
        d = target - num 
        ans = bestSum(d,arr)
        # print(f"Target:{d} ans:{ans}")
        if ans!=None:
            # print(f"ans:{ans} num:{num}")
            ans.append(num)
            # print(shortestCombination)
            if (shortestCombination==None) or len(shortestCombination)>len(ans):
                shortestCombination = ans

    # print("\n")
    return shortestCombination



print(bestSum(7,[7,5,3,4]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
# print(bestSum(100,[1,2,50,25]))
