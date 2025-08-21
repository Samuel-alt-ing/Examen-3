import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter


# ------------------------------------------------------
# SEÑAL SENO
def continuous_sine():
    frequency = 2
    amplitude = 1
    number_of_points = 1000
    time_initial = -1
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)

    continuous_plotter(
        time, x_t,
        'Continuous Sine wave Signal', 'Sin wave Signal',
        'Time [s]',  'Amplitude')


def discrete_sine():
    frequency = 2
    amplitude = 1
    fs = 20
    ts = 0.01
    samples = 100
    n = np.arange(samples)
    x_n = amplitude * np.sin(2 * np.pi * frequency * n * ts )

    discrete_plotter(
        n, x_n,
        'Discrete Sine wave Signal', 'Sin wave Signal',
        'Time [n = index of sample]',  'Amplitude')


# -----------------------------------------------------------------
# SEÑAL EXPONENCIAL
def continuous_exponential():
    number_of_points = 1000
    time_initial = -1
    time_final = 5
    t_cont = np.linspace(time_initial,time_final,number_of_points)
    u_cont = np.where(t_cont >= 0, 1, 0)
    x_cont = np.exp(-2 * t_cont) * u_cont

    continuous_plotter(
        t_cont, x_cont,
        'Continuous exponential wave Signal', 'exponential wave Signal',
        'Time [s]',  'Amplitude')


def discrete_exponential():
    ts = 0.01  # periodo de muestreo
    time_initial = -1
    time_final = 5
    n = np.arange(int((time_final - time_initial) / ts))  # asegura que se cubra todo el rango
    t_disc = time_initial + n * ts
    u_disc = np.where(t_disc >= 0, 1, 0)
    x_disc = np.exp(-2 * t_disc) * u_disc

    discrete_plotter(
        n, x_disc,
        'Discrete Exponential wave Signal', 'exponential wave Signal',
        'Time [n = index of sample]',  'Amplitude')


# ---------------------------------------------------------------------
# SEÑAL TRIANGULAR
def continuous_triangular():
    frequency = 2
    amplitude = 1
    time_initial = -1
    time_final = 5
    number_of_points = 1000
    t_cont = np.linspace(time_initial, time_final, number_of_points)
    x_cont = signal.sawtooth(2 * np.pi * frequency * t_cont, 0.5)

    continuous_plotter(
        t_cont, x_cont,
        'Continuous triangular wave Signal', 'triangular wave Signal',
        'Time [s]',  'Amplitude')
    

def discrete_triangular():
    ts = 0.01
    frequency = 2
    time_initial = -1
    samples = 100
    n = np.arange(samples)
    t_disc = time_initial + n * ts
    x_disc = signal.sawtooth(2 * np.pi * frequency * t_disc, 0.5)

    discrete_plotter(
        n, x_disc,
        'Discrete triangular wave Signal', 'triangular wave Signal',
        'Time [n = index of sample]',  'Amplitude')


# -------------------------------------------------------------------------
#SEÑAL CUADRADA
def continuous_square():
    frequency = 2
    amplitude = 1
    number_of_points = 1000
    time_initial = -1
    time_final = 5
    t_cont = np.linspace(time_initial,time_final,number_of_points)
    x_cont = signal.square(2 * np.pi * frequency * t_cont)

    continuous_plotter(
        t_cont, x_cont,
        'Continuous square wave Signal', 'square wave Signal',
        'Time [s]',  'Amplitude')
    

def discrete_square():
    ts = 0.01
    frequency = 2
    time_initial = -1
    samples = 100
    n = np.arange(samples)
    t_disc = time_initial + n * ts
    x_disc = signal.square(2 * np.pi * frequency * t_disc)

    discrete_plotter(
        n, x_disc,
        'Discrete square wave Signal', 'square wave Signal',
        'Time [n = index of sample]',  'Amplitude')
