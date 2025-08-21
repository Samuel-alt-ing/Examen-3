import numpy as np
from src.utils.grapher import continuous_plotter


def understanding_freq(des_freq):
    initial_time = 0
    end_time = 5
    frequency = float(des_freq)
    amplitude = 1
    number_of_points = 1000
    time = np.linspace(initial_time, end_time, number_of_points)
    xt = amplitude * np.sin(2 * np.pi * frequency * time)

    continuous_plotter(time, xt,
    'Continuous Sine wave Signal', 'Sin wave Signal',
    'Time [s]', 'Amplitude')
