
def chif():
    global ent
    global ent1
    ent = input("Rantre bonn enferye enteval la : ")
    ent1 = input("Rantre bonn siperye enteval la : ")
    while ent.isdigit()==False or ent1.isdigit()==False:
        print("Ou dwe rantre chif selman ...")
        ent = input("Rantre bonn enferye enteval la : ")
        ent1 = input("Rantre bonn siperye enteval la : ")
    ent = int(ent)
    ent1 = int(ent1)
chif()
while ent>=ent1:
    print("bonn enferye a dwe pi piti ke siperye a ...")
    chif()
    
print("-----------------------------------------------")
print("men nonb pe yo : ")
print("                                     ")
for  i in range(ent,ent1):
    if i%2==0:
        print(i)
        