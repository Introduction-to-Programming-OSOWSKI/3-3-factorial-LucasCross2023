def  factorial(x):
        
    total = x
    
    for i in range (1, x):
        total = total * i
    
    return total 

print(factorial(5))