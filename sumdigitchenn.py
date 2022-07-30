a = "0123456789"+" "
chenn = input("Rantre yon chenn ki kopoze de chif ak espas : ")
for i in range(len(chenn)):#kontwol pou make sure itilizate a rantre chif  ak espas selman
    while not chenn[i]  in a :
        print("Ou dwe rantre chif ak espas selman ...") 
        chenn= input(" Rantre yon chenn ki kopoze de chif ak espas : ")
   
x = chenn.split(" ")

prod = 1
for i in x:
    som = 0
    for l in range(len(i)):
         som =som + int(i[l])
    prod = prod*som
print("---    ----    ----    ----    ----   ----   ----")
print("                                                   ")

print("operasyon saa bay : ",prod)
print("                                                   ")
print("---    ----    ----    ----    ----   ----   ----")

