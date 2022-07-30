print("Chwazi 2 nonb epi chwai yon enteval pou yo tou ")
print("        ............................         ")
print("                                                ")
inter = input("mete enteval enferye a : ")
inter1 = input("mete enteval siperye  a : ")

while inter.isdigit() == False or inter1.isdigit()==False :
    print("ou dwe rantre chif selman [...]")
    inter = input("mete enteval enferye a : ")
    inter1 = input("mete enteval siperye  a : ")
inter = int(inter)
inter1 = int(inter1)

num = input("Rantre 1er nonb lan : ")
num1 =input("Rantre 2 eme nonb lan : ")
while num.isdigit() == False or num1.isdigit()==False :
    print("ou dwe rantre chif selman [...]")
    num = input("Rantre 1er nonb lan : ")
    num1 =input("Rantre eme nonb lan : ")
num = int(num)
num1 = int(num1)
a = False

for i   in range(inter,inter1):
    if num in range(inter,inter1) and num1 in range(inter,inter1):
        break
    else:
        print("nonb yo dwe nan enteval ou te rantre a")
        num = input("Rantre 1er nonb lan : ")
        num1 =input("Rantre eme nonb lan : ")


sum = 0
sum1 = 0
sum2 = 0
sum3 = 0

print("------------------------------------------")
print("                                          ")
print(f"miltipl {num} /pa miltipl {num1} \n")
for i in range(inter,inter1):
    if (i%num)==0 and (i%num1)!=0:
        sum = sum + 1
        print("nonb : ",i,"\t\t")
print(f"total :{sum}")
print("------------------------------------------")
print("                                          ")
print(f"miltipl {num1} /pa miltipl {num} \n")
for i in range(inter,inter1):
    if (i%num)!=0 and (i%num1)==0:
        sum1 = sum1 + 1
        print("nonb : ",i,"\t\t")

print(f"total :{sum1}")
print("------------------------------------------")
print("                                          ")
print(f"miltipl {num} / miltipl {num1} \n")  
for i in range(inter,inter1):
    if (i%num)==0 and (i%num1)==0:
        sum2 = sum2 + 1
        print("nonb : ",i,"\t\t")

print(f"total :{sum2}")
print("------------------------------------------")
print("                                          ")
print(f" pa miltipl {num} /pa miltipl {num1} \n")
for i in range(inter,inter1):
    if (i%num)!=0 and (i%num1)!=0:
        sum3 = sum3 + 1
        print("nonb : ",i,"\t\t")

print(f"total :{sum3}")
