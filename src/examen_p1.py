import numpy as np
from src.utils.grapher import continuous_plotter
from src.utils.grapher import discrete_plotter


def dft():
    
    fm = 0.5   
    fc = 8.0   
    m = 0.5
    fs = 64    
    T = 4      
    N = fs * T

    t = np.arange(N) / fs  

    # Señal
    x = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

    # DFT
    X = np.fft.fft(x)
    freqs = np.fft.fftfreq(N, 1/fs)

    half = N // 2
    freqs = freqs[:half]
    X_magnitude = np.abs(X[:half]) / N

    delta_f = fs / N
    print(f"\n   Resolución en frecuencia Δf = {delta_f:.4f} Hz")

    # Aqui es donde comenzamos a detectar picos espectrales
    threshold = 0.1 * np.max(X_magnitude)
    peak_indices = np.where(X_magnitude > threshold)[0]
    peak_freqs = freqs[peak_indices]
    peak_amps = X_magnitude[peak_indices]

    print("\n   Picos detectados (frecuencia [Hz] - amplitud relativa):\n")
    for f, a in zip(peak_freqs, peak_amps):
        print(f"   {f:.2f} Hz -> {a:.3f}")

    print("\n")
    
    continuous_plotter(
        t, x, 
        'Señal en el tiempo', 'x(t)',
        'Time [s]', 'Amplitude'
    )

    discrete_plotter(
        freqs, X_magnitude,
        'Espectro de magnitud (DFT)', '|x(f)|',
        'Frequency [Hz]', 'Magnitud'
    )