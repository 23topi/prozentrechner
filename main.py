
print("1.G = Grundwert bitte 1 eingeben")
print("2.W = Prozentwert")
print("3.p = Prozentsatz")

def Eingabefunktion():

    # print("Bitte auswählen was Sie berechnen wollen: ")
    eingabe = input("Bitte auswählen was Sie berechnen wollen: ")
    if eingabe == "G" or eingabe == "W" or eingabe == "p":
        return eingabe
    else:
        print("falsch")

def Grundwert():
    print("Bitte W eingeben")
    W = int(input())
    print("Bitte p eingeben")
    p = int(input())
    p = p/100
    G = W/p
    print("der Grundwert beträgt")
    print(G)
def Prozentwert():
    print("Bitte G eingeben")
    G = int(input())
    print("Bitte p eingeben ")
    p = int(input())
    W = G * p/100
    print("der Prozentwert beträgt")
    print(W)
def Prozentsatz():
    print("Bitte G eingeben")
    G = int(input())
    print("Bitte W eingeben")
    W = int(input())
    p = W/G
    print("Der Prozentsatz in Dezimalschreibweise: ")
    print(p)


if Eingabefunktion() == "G":
    Grundwert()
elif Eingabefunktion() == "W":
    Prozentwert()
elif Eingabefunktion() == "p":
    Prozentsatz()
else:
    print("zuviele falsche Eingabe, das Programm wird beendet")

# else:
#  Eingabefunktion()
#  if Eingabefunktion() == "W":
#      Prozentwert()

# elif Eingabefunktion() == "p":
#    Prozentsatz()

# if Eingabefunktion() == "W":

# if Eingabefunktion() == "p":

# else:
#    Eingabefunktion()




