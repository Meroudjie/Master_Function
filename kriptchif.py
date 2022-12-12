
p="0-9-22-13"
li=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def kriptchif():

    j=p.split("-")
    f=""
    for i in j:
        f=f+li[int(i)]
    print(f)
kriptchif()