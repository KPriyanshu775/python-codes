# Printing number in sequence
def nums(n):
    if n == 0:
        return
        
    nums(n - 1)    
    print(n)

nums(5)

def nums(n):   
    if n == 0: 
        return 
    print(n)   
    nums(n - 1)  
    print(n)  
nums(5)   

# Working of the recursion code

def nums(n):              # 2, 9, 16, 23
    if n == 0:            # 3, 10, 17, 24
        return            # 4, 11, 18, 25
    print(n)              # 5, 12, 19, 26
    nums(n - 1)           # 6, 13, 20, 27
    print(n)              # 7, 14, 21, 28

nums(5)                   # 1, 8, 15, 22

# Finding factorial of a number

def nums(n):
    if n == 0 or n == 1:
        return 1
    return n * nums(n - 1)
print(nums(5))

# reverse a number

#  reverse number
def reverse(n):
    if n == 0:
        return
    print(n % 10)
    reverse(n // 10)
reverse(12345)
