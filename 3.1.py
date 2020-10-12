minn=int(input("Hur lång tid använder du för att ringa per månad?: "))#Tar reda på hur många minuter
if minn>0 and minn<=33:#Kollar att nummret var inom den logiska operatören
    print("Välj kontant")#Skriver ut om den var inom den logiska operatören
elif minn>33 and minn <=66: #Kollar att nummret var inom den logiska operatören
    print("Välj normal")#Skriver ut om den var inom den logiska operatören
elif minn>66 and minn <=100000: #Kollar att nummret var inom den logiska operatören
    print("Välj plus")#Skriver ut om den var inom den logiska operatören