import matplotlib.pyplot as plt
import numpy as np


def analizar_dac(bits):
    V_FS = 5.0 

    niveles = 2**bits
    paso = V_FS / (niveles - 1)
    resolucion = (paso / V_FS) * 100

    print(f"Número de bits: {bits}")
    print(f"Número de niveles: {niveles}")
    print(f"Tamaño del paso: {paso:.6f} V")
    print(f"Resolución porcentual: {resolucion:.6f} %")

    entrada_digital = np.arange(niveles)
    salida_analogica = entrada_digital * paso

    plt.figure(figsize=(8, 5))
    plt.step(entrada_digital, salida_analogica, where='post', label='Salida del DAC')
    plt.xlabel('Entrada digital')
    plt.ylabel('Salida analógica (V)')
    plt.title(f'Salida de un DAC de {bits} bits')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


