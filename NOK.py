
while True:
    
    antye = input ("rantre yon antye : ")
    while antye.isdigit() == False:
            print("ou dwe rantre chif selman[...]")
            antye = input ("rantre yon antye : ")
            if antye.isdigit() ==True:
                break
    antye = int(antye)
    if antye%4==0:
        print("OK")
    else:
        print("NOK")
    option = input("peze nenpot touch pouw kontinye oubyen  [k] siw vle kite pwogram nan : ")
    if option =="k".lower():
        break

