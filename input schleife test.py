
def Eingabefunktion():
    print("1.G = Grundwert")
    print("2.W = Prozentwert")
    print("3.p = Prozentsatz")

    eingabe = input("Bitte eine W, G oder p eingeben: ")
    if eingabe == "W":
           if eingabe == "G":
                if eingabe == "p":
                    print("zuviele Falscheingaben, das Programm wird beendet")
                else:
                    print("p wird berechnet")
           else:
               print("G wird berechnet")
    else:
          print("W wird berechnet")
Eingabefunktion()

# Version 1.2
