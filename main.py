import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

# ---------------- Función DFT ----------------
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

    # Detección de picos
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


# ---------------- Función examen_p2 ----------------
def examen_p2():
    fs = 256      
    T = 6         
    N = fs * T    
    n = np.arange(N)
    t = n / fs    

    f1 = 8        
    f2 = 20       
    fr = 50       # con ruido

    # Señal discreta limpia
    x_clean = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

    # DFT 
    X_clean = np.fft.fft(x_clean)
    freqs = np.fft.fftfreq(N, 1/fs)
    half = N // 2
    freqs = freqs[:half]
    X_clean_mag = np.abs(X_clean[:half]) / N

    # Señal discreta con ruido
    noise = 0.7 * np.sin(2 * np.pi * fr * t)  # ruido senoidal a 50 Hz
    x_noisy = x_clean + noise

    # DFT
    X_noisy = np.fft.fft(x_noisy)
    X_noisy_mag = np.abs(X_noisy[:half]) / N

    delta_f = fs / N
    print(f"\n   Resolución en frecuencia Δf = {delta_f:.4f} Hz")

    # Detección de picos
    threshold_clean = 0.1 * np.max(X_clean_mag)
    threshold_noisy = 0.1 * np.max(X_noisy_mag)

    peaks_clean = np.where(X_clean_mag > threshold_clean)[0]
    peaks_noisy = np.where(X_noisy_mag > threshold_noisy)[0]

    print("\n   Picos señal limpia:\n")
    for idx in peaks_clean:
        print(f"   {freqs[idx]:.2f} Hz -> {X_clean_mag[idx]:.3f}")

    print("\n   Picos señal con ruido:\n")
    for idx in peaks_noisy:
        print(f"   {freqs[idx]:.2f} Hz -> {X_noisy_mag[idx]:.3f}")

    continuous_plotter(
        t, x_clean,
        "Señal discreta limpia", "x[n]",
        "Tiempo [s]", "Amplitud"
    )

    discrete_plotter(
        freqs, X_clean_mag,
        "DFT señal limpia", "|X(f)|",
        "Frecuencia [Hz]", "Magnitud"
    )

    continuous_plotter(
        t, x_noisy,
        "Señal discreta con ruido", "x[n]+ruido",
        "Tiempo [s]", "Amplitud"
    )

    discrete_plotter(
        freqs, X_noisy_mag,
        "DFT señal con ruido", "|X(f)|",
        "Frecuencia [Hz]", "Magnitud"
    )


# ---------------- Main ----------------
if __name__ == "__main__":
    print("\n------ Ejecutando DFT ------")
    dft()
    
    print("\n------ Ejecutando examen_p2 ------")
    examen_p2()
