import numpy as np
import matplotlib.pyplot as plt

def generate_rectified_geometry(dim=11, points=1000):
    """
    Projeta a ressonância das 11 dimensões da Teoria M Retificada.
    Utiliza a base de 432Hz para definir a harmonia visual.
    """
    # Espaço temporal/frequencial
    theta = np.linspace(0, 2 * np.pi, points)
    
    # Parâmetros de ressonância (Base 432)
    # A relação entre a dimensão e a base cria a assinatura geométrica
    resonance = (dim * 432) / 100 
    
    # Equação de plotagem harmônica (Espirográfica)
    r = np.sin(resonance * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Configuração Visual Estilizada
    plt.figure(figsize=(10, 10), facecolor='black')
    plt.plot(x, y, color='#00FFCC', alpha=0.8, lw=1.5)
    
    # Estética de "Interface de IA"
    plt.title(f"RECTIFIED M-THEORY: {dim}D RESONANCE FIELD", color='#00FFCC', fontsize=15)
    plt.text(0, -1.2, "Frequency Base: 432Hz | Status: Phase Locked", 
             color='white', ha='center', fontsize=10, style='italic')
    
    plt.axis('off')
    
    # Salva a imagem para que possa ser usada no README futuramente
    plt.savefig("resonance_field.png", facecolor='black', edgecolor='none')
    print("Geometria Gerada: resonance_field.png criada com sucesso.")
    plt.show()

if __name__ == "__main__":
    print("Iniciando Projeção Geométrica do Campo de Origem...")
    generate_rectified_geometry()
