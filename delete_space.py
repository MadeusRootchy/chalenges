txt = input("Rantre yon text kelkonk : ")
for i in txt:
    if i ==" ":
        txt = txt.replace(i,"")
print(txt)