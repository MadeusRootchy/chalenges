f = "0123456789"+"."
ipad =input("rantre adress ip a laaa : ")
while len(ipad)> 15 or len(ipad)< 15:#kontwol pou make sure li rantre adres ip a nan foma nomal li
    print("ou dwe rantre 15 karakte...")
    ipad =input("Rerantre adress ip a laaa : ")

while  ipad[3]!="." or ipad[7]!="." or ipad[11]!=".": #kontwol pou make sure li rantre adres ip a nan foma nomal li
    print("  Pa bliye mete pwen [.] apre chak 3 chif ...")
    ipad =input("Rerantre adress ip a laaa : ")

for i in ipad:#kontwol pou make sure itilizate a rantre chif selman
    while not i in f:
        print("Adres Ip a dwe konpoze de chif ak pwen selman") 
        ipad = input("Rerantre adress ip a laaa : ")
a = ipad.split(".")#nou transfome sa itilizate a antre a an lis 
som = 0#inisyalizasyon varyab som ki pral fe som digit yo
for i in a :#nou pakouri lis la
    for n  in i:#nou pakouri chak grenn eleman nan lis la
        som =(som + int(n))*int(a[0][0])# som nan
print("**********************************")        
print("pot la se : ",som)#pot la
