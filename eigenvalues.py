#!/usr/bin/env python

from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100)->list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Cada iteración: 
     1. Factorizamos A^{k-1}= Q * R
     2. Calculamos A^{k}= R* Q    ← ojo: orden invertido

    La matriz A^{k} converge a una matriz (casi) diagonal
    donde cada entrada A[i][j] es un eigenvalor  

    Devuelve la estimación de los eigenvalores
    """


    Ak= A  #A^0 = A original

    for _ in range(n):
        Q,R =qr(Ak)           #paso 1: factorizar
        Ak= matmul(R,Q)       #paso 2: recombinar al revés


    #Los eigenvalores están en la diagonal de Ak
    return [Ak[i][i] for i in range(len(Ak))]        

# ─── Prueba rápida ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Matriz simétrica con eigenvalores conocidos: 1, 2, 3
    A = [
        [2.0, 1.0, 0.0],
        [1.0, 2.0, 1.0],
        [0.0, 1.0, 2.0],
    ]
 
    vals = eigenvals(A, n=100)
    print("Eigenvalores aproximados:")
    for i, v in enumerate(vals):
        print(f"  λ{i+1} = {round(v, 6)}")
 
    # Los valores reales de esta matriz son: 2-√2 ≈ 0.5858, 2, 2+√2 ≈ 3.4142
    import math
    print("\nValores exactos para comparar:")
    print(f"  λ1 = {round(2 - math.sqrt(2), 6)}")
    print(f"  λ2 = {round(2.0, 6)}")
    print(f"  λ3 = {round(2 + math.sqrt(2), 6)}")
 