import numpy as np # Creazione di un alias nell'importazione della libreria esterna
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='blue', linewidth=2, label='Funzione Seno')

plt.title("Il mio primo grafico in Python")
plt.xlabel("Asse X (Tempo in secondi)")
plt.ylabel("Asse Y (Ampiezza)")
plt.grid(True, linestyle='--', alpha=0.7)  # Aggiunge una griglia tratteggiata leggera
plt.legend()  # Mostra il riquadro con il nome della linea (label)

plt.show()