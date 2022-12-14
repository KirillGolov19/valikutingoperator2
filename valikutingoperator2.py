
from math import *
print("Распорядок дня")

try: 
    kell=int(input("Mis kell on praegu"))
    except:
        print("!!!!!")
    if kell==(0):
        print(f"magan")
    elif kell==(1):
        print("magan")
    elif kell==(2):
        print("magan")
    elif kell==(3):
        print("magan")
    elif kell==(4):
        print("magan")
    elif kell==(5):
        print("magan")
    elif kell==(6):
        print("magan")
    elif kell==(7):
        print("tõusis")
    elif kell==(8):
        print("lähen kooli")
    elif kell==(9):
        print("koolis õppides")
    elif kell==(10):
        print("koolis õppides")
    elif kell==(11):
        print("koolis õppides")
    elif kell==(12):
        print("koolis õppides")
    elif kell==(13):
        print("koolis õppides")
    elif kell==(14):
        print("koolis õppides")
    elif kell==(15):
        print("koolis õppides")
    elif kell==(16):
        print("koolis õppides")
    elif kell==(17):
        print("lähen koju")
    elif kell==(18):
        print("kodutõõ tegen")
    elif kell==(19):
        print("kodutõõ tegen")
    elif kell==(20):
        print("vaba aeg")
    elif kell==(21):
        print("vaba aeg")
    elif kell==(22):
        print("vaba aeg")
    elif kell==(23):
        print("vaba aeg")
    elif kell==(00):
        print("vaba aeg")
    elif kell==(01):
        print("magan")

print()
print()
    


#

from random import *
a=randint(0,100)
b=randint(0,100)
print(f"a={a}\b={b}")
if a>b:

    print("{a}, suurem kui {b}")
elif b>a:
    print("{b}, suurem kui {a}")

#

try:
    päev=int(input("Mis päev täna on ?"))
    if  päev==1:
        n="Täna on esmaspäev"
    elif päev==2:
         n="Täna on teisipäev"
    elif päev==3:
         n="Täna on kolmapäev"
    elif päev==4:
         n="Täna on neljapäev"
    elif päev==5:
         n="Täna on reede"
    elif päev==6:
         n="Täna on laupäev"
    elif päev==7:
         n="Täna on pühapäev"
    else:
       print()
except:
    print("Viga")

#
from math import *
from random import *
try: 
    päev=int(input("Mis päev ja mitu tundi täna on?"))
    print(input("Mis päev ja mitu tundi täna on?"))
    if  päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Neljapäev"
        n="5 tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Pühapäev"
        n="0 tundi"
    else: 
        n="Vale number"
    print()
except:
    print("Viga")


#

from math import *
from random import *

r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruudu pindala {Skv} on suurem ringi pindala {Skr}")
    elif Skr>Skv:
        print(f"Ruudu pindala {Skr} on suurem ruudu pindala {Skv}")
    else:
        print("Pindalad on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
print()

#1


#8.2
from math import *
print("Sisselogimine tahvel")
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>=18:
        print("Kas te annate vabenatele loa oma Tahvelit vaadata? ")
        o=(input("Jah või ei. "))
        if o.lower()=="Jah":
            print({o})
            print("See on lihipääs teie vanematele.")
            print("Tahvel on kinni.")

        elif o.upper()=="EI":
        print("Sissepääs puudub. ")
        print("Tahvel on kinni. ")
    if vanus<18:
        print("Juurdepääs vanematele on automaatselt antud. ")
except:
    print("Tahvel on kinni.")
print()
print()
    
