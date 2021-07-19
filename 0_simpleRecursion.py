def recur(n):
    if n==0:
        return 0
    
    print("forword")
    recur(n-1)
    print("backward")


recur(3)