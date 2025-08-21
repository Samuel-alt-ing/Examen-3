import matplotlib.pyplot as plt
import numpy as np
import sys
from src.utils.grapher import continuous_plotter, discrete_plotter


def sine_both(amplitude, frequency, phi):
    t_cont = np.linspace(-1, 5, 1000)
    x_cont = amplitude * np.sin(2 * np.pi * frequency * t_cont + phi)

    Ts = 0.01
    n = np.arange(0, 600)
    t_disc = n * Ts
    x_disc = amplitude * np.sin(2 * np.pi * frequency * t_disc + phi)

    plt.figure(figsize=(10, 5))
    plt.plot(t_cont, x_cont, label='Tiempo continuo', color='blue')
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt='k', label='Tiempo discreto')
    plt.title('Señal seno en tiempo continuo y discreto')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


