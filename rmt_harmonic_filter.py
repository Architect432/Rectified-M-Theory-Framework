import numpy as np

def calculate_harmonic_alignment(frequency):
    """
    Calcula a coerência de um sinal com a Teoria M Retificada.
    Base: 432 Hz | Escala: Phi
    """
    phi = (1 + np.sqrt(5)) / 2
    base_f = 432.0
    
    # Gera os nós das 11 oitavas
    nodes = np.array([base_f * (phi**(i-10)) for i in range(11)])
    
    # Calcula a proximidade com o nó harmônico mais próximo
    diff = np.min(np.abs(frequency - nodes))
    
    return "ALIGNED" if diff < 0.5 else "DISSONANT"

# Exemplo de teste de sinal
if __name__ == "__main__":
    test_freq = 432.0
    status = calculate_harmonic_alignment(test_freq)
    print(f"Signal Frequency: {test_freq}Hz - Status: {status}")
