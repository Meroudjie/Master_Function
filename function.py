import random

def jenalfn(n):
    a="abcdefghijklmnopqrstuvwxyz1234567890"
    code=""
    for i in range(0,n):
        randomA= random.choice(a)
        
        a=a.replace(randomA,"")
        code=code+randomA
        
    print(code)
    
jenalfn(23)
