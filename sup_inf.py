lis = "0123456789"
sup = int(lis[0])
inf = int(lis[0])
for i in range(1,len(lis)):
    
    if int(lis[i]) > sup:
        sup=int(lis[i])
    if int(lis[i])<inf:
        inf=int(lis[i])
print("----------------------------------------")
print("Pi gran nonb nan swit nonb saa se : ",sup)
print("                                         ")
print("Pi piti nonb nan swit nonb saa se : ",inf)

