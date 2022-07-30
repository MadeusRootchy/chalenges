vwayel = "aeiouy"
ch = input("Rantre yon chenn : ")
for i in range(len(ch)) :
    if ch[i] in vwayel:
        ch = ch.replace(ch[i-1],"*")
print(ch)

