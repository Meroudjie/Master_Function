p="Jean-Baptiste Naima"
p=p.replace(" ","-")

p=p.split("-")
initial=""
for i in p:
    initial=initial+i[0]

print(initial)

