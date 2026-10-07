import numpy as np
import matplotlib.pyplot as plt

def analizzatore_traiettorie():
    print("--- 🚀 ANALIZZATORE DI TRAIETTORIE ---")
    
    # 1. Acquisizione dei parametri dall'utente
    try:
        v0 = float(input("Velocità iniziale (m/s) [es. 150]: "))
        theta_deg = float(input("Angolo di lancio (gradi) [es. 60]: "))
        y0 = float(input("Altezza iniziale (m) [es. 0]: "))
        m = float(input("Massa del corpo (kg) [es. 2.0]: "))
        raggio = float(input("Raggio frontale (m) [es. 0.05]: "))
        
        print("\n[INFO] Coefficienti di forma tipici (C_d):")
        print("       Goccia = 0.04 | Sfera = 0.47 | Cilindro = 0.82 | Cubo = 1.05")
        C_d = float(input("Coefficiente aerodinamico (C_d): "))
        
    except ValueError:
        print("\n[ERRORE] Devi inserire valori numerici validi. Usa il punto per i decimali.")
        return

    # Costanti fisiche e ambientali
    rho = 1.225       # Densità dell'aria a livello del mare (kg/m^3)
    g = 9.81
    
    # Calcolo dell'area frontale e del coefficiente k complessivo
    area = np.pi * (raggio**2)
    k = 0.5 * rho * C_d * area
    
    # Conversioni e componenti vettoriali iniziali
    theta_rad = np.radians(theta_deg)
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)

    # ==========================================
    # 2. CALCOLO MOTO IDEALE (Vettoriale con NumPy)
    # ==========================================
    t_volo_ideale = (v0y + np.sqrt(v0y**2 + 2 * g * y0)) / g
    t_array = np.linspace(0, t_volo_ideale, 1000) 
    
    x_ideale = v0x * t_array
    y_ideale = y0 + v0y * t_array - 0.5 * g * t_array**2

    # ==========================================
    # 3. CALCOLO MOTO REALE (Integrazione Numerica)
    # ==========================================
    dt = 0.01 
    x_lista, y_lista = [0.0], [y0]
    vx, vy = v0x, v0y
    
    while y_lista[-1] >= 0:
        v = np.sqrt(vx**2 + vy**2)
        
        ax = -(k / m) * v * vx
        ay = -g - (k / m) * v * vy
        
        vx += ax * dt
        vy += ay * dt
        x_lista.append(x_lista[-1] + vx * dt)
        y_lista.append(y_lista[-1] + vy * dt)

    x_reale = np.array(x_lista)
    y_reale = np.array(y_lista)

    # ==========================================
    # 4. ANALISI DATI TRAMITE NUMPY
    # ==========================================
    apogeo_ideale = np.max(y_ideale)
    gittata_ideale = x_ideale[-1]
    
    apogeo_reale = np.max(y_reale)
    gittata_reale = x_reale[-1]
    
    idx_apogeo_reale = np.argmax(y_reale) 
    x_apogeo_reale = x_reale[idx_apogeo_reale]

    print(f"\n--- RISULTATI ANALISI ---")
    print(f"Moto Ideale -> Apogeo: {apogeo_ideale:.1f} m | Gittata: {gittata_ideale:.1f} m")
    print(f"Moto Reale  -> Apogeo: {apogeo_reale:.1f} m | Gittata: {gittata_reale:.1f} m")
    print(f"L'attrito ha ridotto la gittata di {gittata_ideale - gittata_reale:.1f} m")

    # ==========================================
    # 5. RENDERING GRAFICO
    # ==========================================
    plt.figure(figsize=(12, 6))
    
    plt.plot(x_ideale, y_ideale, label='Ideale (Vuoto)', color='gray', linestyle='--', alpha=0.7)
    plt.plot(x_reale, y_reale, label=f'Reale (Attrito, m={m}kg)', color='#d9534f', linewidth=2.5)
    
    plt.plot(x_apogeo_reale, apogeo_reale, 'ko') 
    plt.annotate(f'Apogeo ({apogeo_reale:.1f}m)', 
                 xy=(x_apogeo_reale, apogeo_reale), 
                 xytext=(x_apogeo_reale + 20, apogeo_reale + (apogeo_reale * 0.05)),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=10)

    plt.title('Analisi Traiettoria Balistica', fontsize=16, fontweight='bold')
    plt.xlabel('Distanza Orizzontale $x$ (m)', fontsize=12)
    plt.ylabel('Altitudine $y$ (m)', fontsize=12)
    plt.axhline(0, color='black', linewidth=1.5) 
    plt.grid(True, linestyle=':', alpha=0.8)
    plt.legend(loc='upper right', fontsize=11)
    
    plt.xlim(left=0)
    plt.ylim(bottom=0)

    plt.show()

if __name__ == "__main__":
    analizzatore_traiettorie()