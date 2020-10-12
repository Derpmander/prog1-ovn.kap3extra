minn=int(input("Hur lång tid använder du för att ringa per månad?: "))
if minn>0 and minn<=33:
    print("Välj kontant")
elif minn>33 and minn <=66:
    print("Välj normal")
elif minn>66 and minn <=100000:
    print("Välj plus")