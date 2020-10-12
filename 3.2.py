import math#importera math
rad=input("Vad är cirkelns radie: ") #tar reda på cirkelns radie
x=float(rad)#gör om str till float
if x>0: #gör så att om radien är större än 0 så fortsäter den räkna
    y=3.141#radien
    area=x*x*y#räknar ut arean
    print(f"arean är {area:2.3f}")#skriver ut arean
    z=x+x#räknar ut diamentern
    omkrets=z*y#räknar ut omkrets
    print(f"omkretsen är {omkrets:2.3f}")#skriver ut omkretsen
else:
    print("error")#skriver ut error om det var mindre än noll