#!/usr/bin/env python
 
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
from main import interpolate_sine, evaluar_polinomio, linspace
 
 
def hacer_gif(n_max: int = 100, archivo: str = 'interpolacion.gif'):
    """
    Genera un GIF que muestra cómo mejora la interpolación
    polinomial de sin(x) al ir de 2 hasta n_max puntos.
 
    FuncAnimation funciona así:
      - Defines una función `actualizar(frame)` que dibuja el estado
        del frame número `frame`
      - Le dices cuántos frames hay en total
      - Ella llama a `actualizar` una vez por frame y guarda cada imagen
    """
 
    # Puntos densos para graficar curvas suaves
    xs = list(linspace(0, 2 * pi, 500))
    seno_real = [sin(x) for x in xs]
 
    # --- Configurar la figura una sola vez ---
    fig, ax = plt.subplots(figsize=(10, 5))
 
    # Línea del seno real (no cambia entre frames)
    ax.plot(xs, seno_real, label='sin(x)', color='steelblue', linewidth=2)
 
    # Línea del polinomio (se actualiza cada frame)
    linea_poly, = ax.plot([], [], color='tomato', linewidth=1.5,
                          linestyle='--', label='Polinomio interpolante')
 
    # Puntos de interpolación (se actualizan cada frame)
    puntos_scatter = ax.scatter([], [], s=20, color='tomato', zorder=5,
                                label='Nodos de interpolación')
 
    ax.set_xlim(0, 2 * pi)
    ax.set_ylim(-1.4, 1.4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
 
    titulo = ax.set_title('')
 
    # --- Función que actualiza cada frame ---
    def actualizar(n):
        """
        n es el número de puntos de interpolación en este frame.
        FuncAnimation la llama automáticamente para cada valor en `frames`.
        """
        coef = interpolate_sine(n)
 
        # Evaluar el polinomio en los 500 puntos densos
        ys_poly = [evaluar_polinomio(coef, x) for x in xs]
 
        # Actualizar la línea del polinomio
        linea_poly.set_data(xs, ys_poly)
 
        # Actualizar los puntos de interpolación
        puntos_x = list(linspace(0, 2 * pi, n))
        puntos_y = [sin(x) for x in puntos_x]
        puntos_scatter.set_offsets(list(zip(puntos_x, puntos_y)))
 
        # Actualizar el título
        titulo.set_text(f'Interpolación polinomial de sin(x) — {n} puntos')
 
        return linea_poly, puntos_scatter, titulo
 
    # --- Crear la animación ---
    # frames: lista de valores que se pasan a `actualizar` uno por uno
    # interval: milisegundos entre frames
    # blit=True: solo redibuja lo que cambió (más eficiente)
    anim = animation.FuncAnimation(
        fig,
        actualizar,
        frames=range(2, n_max + 1),
        interval=80,
        blit=True
    )
 
    # --- Guardar como GIF usando Pillow ---
    anim.save(archivo, writer='pillow', fps=12)
    plt.close()
    print(f"GIF guardado como {archivo}")
 
 
if __name__ == "__main__":
    hacer_gif(n_max=100, archivo='interpolacion.gif')