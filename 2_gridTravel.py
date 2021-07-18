def gridTravel(m,n):
    if m==1 and n==1:
        return 1
    elif m==0 or n==0:
        return 0
    
    return gridTravel(m-1,n)+gridTravel(m,n-1)


print(gridTravel(3,3))
print(gridTravel(2,3))
# print(gridTravel(18,18))


# MEMOIZATION

hash = {}
def memoGrid(m,n):
    key = (m,n)
    rev_key = (n,m)
    if key in hash:
        return hash[key]
    elif rev_key in hash:
        return hash[rev_key]
    elif (m==1 and n==1):
        return 1
    elif (m==0 or n==0):
        return 0

    
    hash[key] = memoGrid(m-1,n)+memoGrid(m,n-1)
    return hash[key]


print(memoGrid(3,3))
print(memoGrid(40,400))