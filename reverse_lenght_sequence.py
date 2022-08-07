sec = [0,1,2,3,4]
rev=[]
def fonc(N):
    a = -1
    for i in range(len(sec)):
        if i ==0:
            rev = sec[a::-1]
        else:
            rev = rev[a::-1]+rev[a+1:len(rev)]
        a -=1
    print(rev)
    for i,el in enumerate(rev):
        if el == N:
            print(f"element :{el} \n Index :{i} ")
 
fonc(4)