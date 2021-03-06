# def canConstruct(target,wordBank):
#     if target=="":
#         return True 


#     for word in wordBank:
#         if target.find(word)==0:
#             remain = target[len(word):]
#             ans = canConstruct(remain,wordBank)
#             if ans!=False:
#                 return True 
    
#     return False 



def canConstruct(target,wordBank,memo={}):
    if target in memo:
        return memo[target]
    elif target=="":
        return True 
    
    for word in wordBank:
        if target.find(word)==0:
            remain = target[len(word):]
            ans = canConstruct(remain,wordBank)
            if ans==True:
                memo[target]=True
                return True 
    
    memo[target] = False 
    return False 



print(canConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(canConstruct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',["e",'ee','eee','eeee','eeeee','eeeeee']))