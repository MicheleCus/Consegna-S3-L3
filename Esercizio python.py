import math

def calcola_perimetro_quadrato(lato):
    return lato * 4

def calcola_perimetro_cerchio(raggio):
    return raggio * math.pi * 2

def calcola_perimetro_rettangolo(base,altezza):
    return (base + altezza) * 2
# Definisco le varie funzioni che mi servono per il calcolo dei perimetri
def main():
    while True: 

        print("Calcola il perimetro delle seguenti figure")
        print("Quadrato")
        print("Cerchio")
        print("Rettangolo")
        print("Esci")
        scelta = input("Seleziona una figura geometrica oppure esci: ")
        if scelta == "Esci":
            print("Ciao")
            break
        elif scelta == 'Quadrato':
            lato = float(input("Inserisci il lato del quadrato "))
            perimetro = calcola_perimetro_quadrato(lato)
            print(f"Il perimetro del quadrato è: {perimetro}")
        elif scelta == 'Cerchio':
            raggio = float(input("Inserisci il raggio del cerchio "))
            perimetro = calcola_perimetro_cerchio(raggio)
            print(f"La circonferenza è: {perimetro}")
        elif scelta == 'Rettangolo':
            base = float(input("Inserisci la base "))
            altezza = float(input("Inserisci l'altezza "))
            perimetro = calcola_perimetro_rettangolo(base, altezza)
            print(f"Il perimetro del rettangolo è: {perimetro}")
        else:
            print(f"Scelta non valida.")
#La main function è di tipo while, così il programma può effettuare più calcoli fino  a quando non termina le operazioni
if __name__ == "__main__":
    main()
    
