x = input("rantre yon premye nonb : ")
y = input("rantre yon dezyem nonb : ")
while x.isdigit()==False or y.isdigit()==False:
    print("ou dwe rantre chif selman...")
    x = input("rantre yon premye nonb : ")
    y = input("rantre yon dezyem nonb : ")
y = int(y)
x = int(x)

if x < y:
    print((y/x)/2)
else:
        print((x/y)/2)

