#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

from gram_schmidt import gm, transpose, dot

def qr(M: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """Realiza la factorización QR de una matriz M.
 
    Q: matriz cuyas columnas son los vectores ortonormales (unitaria)
    R: matriz triangular superior
 
    Idea:
      - Las columnas de M son los vectores que le pasamos a Gram-Schmidt
      - Gram-Schmidt nos devuelve columnas ortonormales → esas forman Q
      - R se obtiene como Q^T * M  (porque A = QR  =>  Q^T A = Q^T QR = IR = R)
    """
    # 1. Extraemos las columnas de M  (M está guardada como lista de filas)
    columnas = transpose(M)          # cada elemento es una columna de M
 
    # 2. Aplicamos Gram-Schmidt a las columnas → obtenemos columnas ortonormales
    columnas_Q = gm(columnas)        # lista de vectores ortonormales
 
    # 3. Q se arma poniendo esas columnas ortonormales de vuelta como matriz
    #    columnas_Q tiene forma [[col0], [col1], ...]  así que trasponemos
    Q = transpose(columnas_Q)
 
    # 4. R = Q^T * M
    #    Como Q es unitaria, Q^T = Q^{-1}, entonces Q^T * M = R (triangular sup.)
    Qt = transpose(Q)
    n = len(M)
    R = [[dot(Qt[i], [M[k][j] for k in range(n)]) for j in range(n)]
         for i in range(n)]
 
    # Limpieza numérica: valores muy pequeños bajo la diagonal los ponemos en 0
    # (errores de punto flotante que deberían ser exactamente 0)
    for i in range(n):
        for j in range(i):          # j < i  →  debajo de la diagonal
            if abs(R[i][j]) < 1e-10:
                R[i][j] = 0.0
 
    return Q, R



# ─── Prueba rápida ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from gram_schmidt import matrix_to_str
 
    M = [
        [1.0, 1.0, 0.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0],
    ]
 
    Q, R = qr(M)
 
    print("Q (debe ser unitaria — columnas ortonormales):")
    print(matrix_to_str([[round(x, 6) for x in fila] for fila in Q]))
 
    print("\nR (debe ser triangular superior):")
    print(matrix_to_str([[round(x, 6) for x in fila] for fila in R]))
 
    # Verificación: reconstruir M = Q * R
    from gram_schmidt import matmul
    QR = matmul(Q, R)
    print("\nQ * R (debe ser igual a M original):")
    print(matrix_to_str([[round(x, 6) for x in fila] for fila in QR]))
 
    # Verificación: Q^T * Q debe ser la identidad
    Qt = [[Q[k][i] for k in range(len(Q))] for i in range(len(Q[0]))]
    QtQ = matmul(Qt, Q)
    print("\nQ^T * Q (debe ser la identidad):")
    print(matrix_to_str([[round(x, 6) for x in fila] for fila in QtQ]))
