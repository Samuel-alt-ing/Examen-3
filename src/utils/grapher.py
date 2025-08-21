import matplotlib.pyplot as plt


def continuous_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def discrete_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.stem(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


# utils/grapher.py
import matplotlib.pyplot as plt

def graficar_senal(x, y, tipo='continua', titulo='Señal', xlabel='Eje X', ylabel='Eje Y'):
    """
    Grafica una señal en tiempo o frecuencia.

    Parámetros:
    - x: array-like, eje horizontal (tiempo o frecuencia)
    - y: array-like, eje vertical (amplitud o magnitud)
    - tipo: 'continua' o 'discreta'
    - titulo, xlabel, ylabel: etiquetas del gráfico
    """
    plt.figure(figsize=(8, 4))

    if tipo == 'continua':
        plt.plot(x, y, '-b', label=titulo)
    elif tipo == 'discreta':
        plt.stem(x, y, basefmt=" ", use_line_collection=True, label=titulo)
    else:
        raise ValueError("El parámetro 'tipo' debe ser 'continua' o 'discreta'")

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
