import numpy as np
import matplotlib.pyplot as plt


# Побудова кубічного сплайну
def cubic_spline(x, y, c, h, N):

    a = y[:-1]
    b = np.zeros(N)
    d = np.zeros(N)

    for i in range(N):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return a, b, c, d


# Функція для побудови графіків
def plot_functions(x, y, a, b, c, d, x0, xn, N, f):

    x_plot = np.linspace(x0, xn, 1000)
    y_plot = f(x_plot)

    # Інтерпольовані значення
    y_interpolated = np.zeros_like(x_plot)

    for i in range(N):
        mask = (x_plot >= x[i]) & (x_plot <= x[i + 1])
        dx = x_plot[mask] - x[i]
        y_interpolated[mask] = (
            a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
        )

    # Помилка інтерполяції
    error = y_plot - y_interpolated

    # Графіки
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(x_plot, y_plot, label='f(x)', color='blue', linewidth=2)
    plt.title('Original Function f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(x_plot, y_interpolated,
             label='Cubic Spline Interpolation',
             color='green', linewidth=2)
    plt.title('Cubic Spline Interpolation')
    plt.xlabel('x')
    plt.ylabel('Interpolated N(x)')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(x_plot, error,
             label='Interpolation Error',
             color='red', linewidth=2)
    plt.title('Interpolation Error e(x)')
    plt.xlabel('x')
    plt.ylabel('e(x)')
    plt.legend()

    plt.tight_layout()
    plt.show()


# ===============================
# МІНІМАЛЬНИЙ ЗАПУСК (додано)
# ===============================

def f(x):
    return np.sin(x)


x0 = 0
xn = 5
N = 5

x = np.linspace(x0, xn, N + 1)
y = f(x)

h = np.diff(x)

# тимчасово коефіцієнти c (як у твоєму коді)
c = np.zeros(N + 1)

a, b, c, d = cubic_spline(x, y, c, h, N)

plot_functions(x, y, a, b, c, d, x0, xn, N, f)