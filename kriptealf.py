

li=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def kripte():
    p="mot"
    K=""
    for i in p:
        K=K+str(li.index(i))
        K=K+"-"
    K=K[:-1]
    print(K)
        
kripte()
