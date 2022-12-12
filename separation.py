
def separate(p):
    
    s=""
    for i in p :
        s=s+i+","

    return s

p=input("Entrer un mot:")    
r=separate(p)
print("la separation est:",r)
