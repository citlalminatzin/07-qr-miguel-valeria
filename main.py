#!/usr/bin/env python

import collections
import numbers

from math import pi, sin
from collections.abc import Sequence 
import matplotlib.pyplot as plt
from linear_solver import solve

# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(Sequence):
    """linspace(start, stop, num) -> linspace object
    
    Return a virtual sequence of num numbers from start to stop (inclusive).
    
    If you need a half-open range, use linspace(start, stop, num+1)[:-1].
    """
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  

def vandermonde_matrix(x: list[float])->list[list[float]]:
    """Genera una matriz de Vandermonde"""
    n = len(x)
    return[[xi**j for j in range(n)] for xi in x]
    
def interpolate(points: list[float], values: list[float]) -> list[float]:
    """
    Interpola un polinomio a los puntos

    Devuelve los coeficientes del polinomio
    """
    
    M = vandermonde_matrix(points)
    return solve(M, values)


def interpolate_sine(n:int)->list[float]:
    """Recibe la cantidad de puntos a interpolar la función seno"""
    lim_inf:float = 0
    lim_sup:float = 2 * pi
    
    #generar los puntos
    points = linspace(lim_inf, lim_sup, n)
    
    #evaluar seno en esos puntos
    valores = [sin(x) for x in points]
    
    return interpolate(list(points), valores)
    

def evaluar_polinomio(coef: list[float], x: float) -> float:
    """Evalúa el polinomio con coeficientes `coef` en el punto x."""
    return sum(c * x**j for j, c in enumerate(coef))



def graficar_interpolacion(n: int = 100):
    """
    Grafica la interpolación polinomial del seno con n puntos
    junto a la función seno real.
    """
    # Calcular coeficientes del polinomio interpolante
    coef = interpolate_sine(n)
 
    # Puntos densos para que la curva se vea suave
    xs = list(linspace(0, 2 * pi, 500))
 
    seno_real = [sin(x) for x in xs]
    polinomio = [evaluar_polinomio(coef, x) for x in xs]
 
    # Puntos de interpolación (los nodos)
    puntos_x = list(linspace(0, 2 * pi, n))
    puntos_y = [sin(x) for x in puntos_x]
 
    fig, ax = plt.subplots(figsize=(10, 5))
 
    ax.plot(xs, seno_real,
            label='sin(x)', color='steelblue', linewidth=2)
    ax.plot(xs, polinomio,
            label=f'Polinomio interpolante ({n} puntos)',
            color='tomato', linewidth=1.5, linestyle='--')
    ax.scatter(puntos_x, puntos_y,
               s=15, color='tomato', zorder=5, label='Nodos de interpolación')
 
    ax.set_title(f'Interpolación polinomial de sin(x) con {n} puntos en [0, 2π]')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, alpha=0.3)
 
    plt.tight_layout()
    plt.savefig('interpolacion.png', dpi=150)
    plt.show()
    print("Gráfica guardada como interpolacion.png")


if __name__ == "__main__":
# Puntos de entrada
    x = [0, 1, 2]

    V = vandermonde_matrix(x)

    print("Matriz de Vandermonde:")
    for fila in V:
        print(fila)
        
    puntos = [0, 1, 2]
    valores = [1, 4, 9]
    coef = interpolate(puntos, valores)
    coef_redondeado = [round(c, 6) for c in coef] #redondeamos los valores 
    print("Coeficientes del polinomio:")
    print(coef_redondeado)
    
    coeficientes = interpolate_sine(5)
    print("Coeficientes del polinomio interpolante del seno:")
    print(coeficientes)
    # Graficar la interpolación del seno
    graficar_interpolacion(n=100)


    
    