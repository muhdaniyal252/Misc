def solution(n,x,y):
    if n > 1: 
        return solution(n-1,x,y) + solution(n-2,x,y)
    elif n == 1:
        return y
    else: 
        return x
    
