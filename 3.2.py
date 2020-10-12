import math#importera math
rad=input("Vad är cirkelns radie: ") #tar reda på cirkelns radie
x=float(rad)#gör om str till float
if x>0: #gör så att om radien är större än 0 så fortsäter den räkna
    y=3.141
    area=x*x*y
    print(f"arean är {area:2.3f}")
    z=x+x
    omkrets=z*y
    print(f"omkretsen är {omkrets:2.3f}") 
else:
    print("error")