# Programma che calcola il moto del proiettile o piu in generale di un razzo
# Importazione di librerie fondamentali per il calcolo delle varie funzioni
from math import sin, cos, radians, pow

#Definizione delle costanti fondamentali per l'esecuzione del programma
ACCELERAZIONE_GRAVITA = 9,81 # Calcolato in m/s^2

#definizione ed implementazione delle funzioni del programma
def tempo_volo(velocita_iniziale, angolo_iniziale):
    angolo_radianti = radians(angolo_iniziale)
    tempo = (2*velocita_iniziale * sin(angolo_radianti)) / 9.81 #In questo modo ottengo il tempo di volo del corpo
    return tempo

def x_finale(x_iniziale, velocità_iniziale, angolo_iniziale, tempo):
    angolo_radianti = radians(angolo_iniziale)
    x_finale = x_iniziale + velocita_iniziale*cos(angolo_radianti)*tempo
    return x_finale

def forza_attrito_aria(velocita_iniziale, coefficiente_resistenza, area_perpendicolare):
    forza = 0.5 * 1,225 * pow(velocita_iniziale, 2) * coefficiente_resistenza * area_perpendicolare
    return forza

# come presupposto mettiamo che l'oggetto parta dalla posizione xi, yi ed arrivi a y = 0 ed x incognita 
velocita_iniziale = int(input("Inserisci la velocità iniziale dell'oggetto: "))
angolo_iniziale = int(input("Inserisci l'angolo iniziale dell'oggetto, considerando l'inclinazione in gradi rispetto all'asse delle x: "))
x_iniziale = int(input("Inserisci la posizione x iniziale dell'oggetto: "))
y_iniziale = int(input("Inserisci la posizione y iniziale dell'oggetto: "))

tempo = tempo_volo(velocita_iniziale, angolo_iniziale)
x_finale = x_finale(x_iniziale, velocita_iniziale, angolo_iniziale, tempo)

# coefficiente_resistenza = int(input("Inserisci il coefficiente di resistenza dell'aria: "))
# area_perpendicolare = int(input("Inserisci l'area perpendicolare all'attrito dell'aria: "))
# forza = forza_attrito_aria(velocita_iniziale, coefficiente_resistenza, area_perpendicolare)

print(f"Il proiettile in posizione ({round(x_iniziale, 1)},{round(y_iniziale, 1)}), velocità di {round(velocita_iniziale, 1)} m/s ed angolazione di {round(angolo_iniziale, 1)} gradi ha una posizione finale x di {round(x_finale, 1)} m e un tempo di volo di {round(tempo, 1)} s")

# print(f"L'attrito dell'aria complessiva sull'oggetto è di {round(forza, 1)} N!")

