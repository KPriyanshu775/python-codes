# Printing number in sequence
def nums(n):
    if n == 0:
        return
        
    nums(n - 1)    
    print(n)

nums(5)