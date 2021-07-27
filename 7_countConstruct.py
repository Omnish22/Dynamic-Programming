# def countConstruct(target,wordBank):
#     if target=="":
#         return 1 
#     counts = 0
#     for word in wordBank:
#         if target.find(word)==0:
#             remain = target[len(word):]
#             ans = countConstruct(remain,wordBank)
#             if ans!=0:
#                 counts += ans
#     return counts 



def countConstruct(target,wordBank,memo={}):
    if target in memo:
        return memo[target]
    elif target=="":
        return 1
    count = 0
    for word in wordBank:
        if target.find(word)==0:
            remain = target[len(word):]
            ans = countConstruct(remain,wordBank)
            if ans!=0:
                count += ans
    memo[target]=count
    print(memo)
    return count  


print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countConstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct('enterapotentpot',['a','p','ent','enter','ot','o','t']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',["e",'ee','eee','eeee','eeeee','eeeeee']))