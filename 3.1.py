minn=int(input("Hur lång tid använder du för att ringa per månad?: "))
if minn>0<=33:
    print("kontant")
elif minn<33>=66:
    print("normal")
elif minn<66>=100000:
    print("plus")
else:
    print ("YOU FUCKED UP")