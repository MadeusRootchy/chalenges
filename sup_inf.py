a = "0123456789"+" "
b = "                                                      "
lis = input("rantre kek nonb  : ")

# print(len(lis))
# for j in range(len(lis)):
#     if lis[j]==" " and lis[j+1]==" " or lis[j]==" " and lis[j-1]==" " :

#         lis = lis.replace(lis[j],"")
   
for i in range(len(lis)):#kontwol pou make sure itilizate a rantre chif  ak espas selman
    while not lis[i]  in a :
        print("Ou dwe rantre chif ak espas selman ...") 
        chenn= input(" Rantre yon chenn ki kopoze de chif ak vigil selman : ")
# for i in lis:
#     if i in b:
x = lis.split(i)
sup = int(x[0])
inf = int(x[0])
for i in range(1,len(x)):
    
    if int(x[i]) > sup:
        sup=int(x[i])
    if int(x[i])<inf:
        inf=int(x[i])
print("----------------------------------------")
print("Pi gran nonb nan swit nonb saa se : ",sup)
print("                                         ")
print("Pi piti nonb nan swit nonb saa se : ",inf)

