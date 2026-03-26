[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/y6M6hpgi)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23298888)
# Factorización QR

¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO

## Integrantes

- Juro por Amogasiddhi que si no me escriben los integrantes de su equipo empezando por apellido y ordenados de forma alfabética, lloro

## Objetivos

1. Programar factorización QR en Python puro
2. Aplicar la factorización QR para obtener los valores propios de una matriz
3. Aplicar la factorización QR para la solución de sistemas de ecuaciones lineales
4. Aplicar la factorización QR en la interpolación de polinomios

## Instrucciones

Realiza los entregables en Python puro. Es decir, deberías poder ejecutar todo tu código en un entorno con solamente un Python recién instalado, sin paqueterías externas. La única excepción es para la graficación en el último entregable.

## ¿Qué demonios es la factorización QR?

Vamos a utilizar esta factorización para aproximar los valores propios de un operador lineal. Para entender este algoritmo primero es necesario retomar algunas definiciones de Álgebra Lineal 1.

### Conceptos básicos

**Producto interior.** Sea $V$ un espacio vectorial sobre el campo $K$, decimos que una función $<\cdot,\cdot>:V\times V\to K$ es un producto interior si cumple con las siguientes propiedades:


*   **Postiva**. Para toda $v\in V$, $$<v,v>\geqslant 0$$
*   **Definida**. $<v,v> = 0$ si y sólo si $v=0$
*   **Aditividad en el primer argumento**. Para todo $u,v,w\in V$, $$<u+v,w>=<u+w>+<v,w>$$
*   **Homogeneidad en el primer argumento**. Para todo $\lambda\in K$ y para todo $u,v\in V$ se cumple que $$<\lambda u,v>=\lambda<u,v>$$
*   **Simetría conjugada**. Para todo $u,v\in V$, $$<u,v> = \overline{<v,u>}$$

Si podemos definir este tipo de función sobre $V$, podemos dotarle de mucha estructura. La última propiedad nos permite definir productos puntos sobre campos complejos. Pero en el caso de los reales ($\mathbb{R}$), $x=\overline{x}$.

_Ejemplo._ Sobre $\mathbb{R}^n$ podemos definir al producto punto tal que

$$x\cdot y=\sum_{k=1}^n x_ky_k=x_1y_1+\cdots+x_ny_n$$

Con $x=(x_1,\cdots,x_n)$, $y=(y_1,\cdots,y_n)$

_Proposición._ $\cdot$ es un producto interior sobre $\mathbb{R}^n$.

El producto interior nos dota de mucha estructura. Particularmente nos permite medir que tán similares son dos vectores entre sí mediante la inducción de una norma y esta a su vez nos puede inducir una medida de medir qué tan lejanos estan los vectores entre sí.

**Norma inducida por el producto punto.** Sea $v\in V$, denotamos la norma inducida por el producto punto $<\cdot,\cdot>$ como

$$\|v\|=\sqrt{<v,v>}$$

_Proposición._ La norma inducida por el producto punto es una norma.


### Ortonormalidad y matrices unitarias

Los vectores de norma uno tienen propiedades especiales. Es así que nos gustaría nombrarlos.

**Lista ortonormal.** Sea una lista de vectores $\{e_1,\cdots,e_n\}$ es ortonormal si cada uno de los vectores tiene norma 1. En otras palabras

$$<e_j,e_k>=\begin{cases}
1&\text{, }j=k,\\
0&\text{, }j\ne k,
\end{cases}$$

Para todo $j,k\in\{1,\cdots,n\}$.

Particularmente si $n=\textrm{dim}\ V$, esta lista es una base de $V$. ¿Qué pasaría si crearamos una matriz que tenga como columnas a una de estas listas?

**Matriz unitaria.** Sea $M\in\textrm{Mat}(n)$ es unitaria si sus columnas forman una lista ortonormal.

Estas matrices cumplen con varias propiedades interesantes, como el que preservan el tamaño (normas) de los vectores y por construcción de las bases ortonormales su traspuesta es su propia inversa. En resumen

_Proposición._ Sea $Q\in\textrm{Mat}(n)$ matriz unitaria, las siguientes proposiciones son equivalentes.

1.   $Q$ es una matriz unitaria
2.   Las filas de $Q$ forman una lista ortonormal $\mathbb K ^n$
3.   $\|Qv\|=\|v\|$ para todo $v\in K^n$
4.   $Q^TQ=QQ^T=I_n$ con $I_n\in\textrm{Mat}(n)$ la matriz identidad.

### La factorización QR

Sea $A\in\textrm{Mat}(n)$ de rango $n$. Entonces existen matrices únicas $Q,R\in\textrm{Mat}(n)$ tal que $Q$ es unitaria, y $R$ es triangular superior con solamente números positivos en su diagonal y que cumplen que:

$$A = QR$$

¿Pero cómo llegamos hasta esta factorización?

### Gram-schmidt

Primero necesitamos generar bases ortonormales. Para ello utilizaremos un algoritmo donde partimos de una base $\{v_1,\cdots,v_n\}$, calculamos

$$u_k = v_k-\sum_{j=1}^{k-1}\textrm{proj}_{u_j}(v_k)$$

con

$$\textrm{proj}_{u}(v) = \frac{<v,u>}{<u,u>}u$$

Así hacemos que $<u_i,u_j>=0$ para $i,j\in\{1,\cdots,n\}$ si $i\ne j$. Ahora necesitamos que cada uno de estos vectores tenga norma $1$, lo cual lo podemos lograr normalizándolos, es decir:

$$e_k=\frac{u_k}{\|u_k\|}$$

> **Entregable 1.** Completa el archivo `gram-schmidt.py` con base en la teoría que discutimos

> **Entregable 2.** Utilizando las funciones que escribiste en el entregable anterior, completa el archivo `qr.py`

## ¿Para qué demonios me sirve la factorización QR?

La factorización QR tiene varias aplicaciones :D. Éstas suelen surgir en contextos más aplicados y varían de campo a campo. Los ejercicios seleccionados son generales. Pero por ejemplo:

- Conocer los valores propios de una matriz de datos puede ayudarnos en la creación de sistemas de recomendación, identificación de temas clave en un texto, etcétera
- Resolver sistemas de ecuaciones lineales nos permite implementar soluciones numéricas a ecuaciones diferenciales ordinarias y parciales (que a su vez son los modelos matemáticos detrás de diversos fenómenos físicos y biológicos)
- Interpolar polinomios tiene aplicaciones en criptografía y graficación por computadora

### Valores propios

¡Calculemos los valores propios de una matriz! Llamémosla $A\in\textrm{Mat}(n)$ con $n\in\mathbb{Z}^+$ con factorización $A=QR$. Un posible algoritmo para el cálculo de los eigenvalores es el siguiente:

*Algoritmo 1. Eigenvalores mediante QR*
1. $A^{(0)}=A$
2. **for** $k=1,2,\dots$
    1. $Q^{(k)}R^{(k)}=A^{(k-1)}$
    2. $A^{(k)}=R^{(k)}Q^{(k)}$

Donde $A^{(k)}$ es la $k$-ésima iteración de la matriz $A$. Este algoritmo converge a una matriz diagonal donde cada entrada es un eigenvalor.

> **Entregable 3.** Completa el código en `eigenvalues.py` 

### Sistemas de ecuaciones lineales

Hay varios algoritmos de solución de sistemas de ec. lineales. Particularmente, el hecho de que la factorización QR nos da una matriz triangular facilita el proceso de solucionar un sistema de ecuaciones lineales. Empezamos desde la última fila, donde obtenemos el valor de la incógnita; posteriormente subimos utilizando el valor obtenido previamente.

Para ello podemos usar el siguiente algoritmo:

*Algoritmo 2. Mínimos cuadrados vía factorización QR.* Dado el sistema de ecuaciones lineales $Ax=b$
1. Calcula la factorización QR de $A$
2. Calcula el vector $Qb$
3. Soluciona el sistema triangular superior $Rx=Qb$ para el vector $x$

> **Entregable 4.** Completa el código en `linear_solver.py`

### Interpolación de polinomios

Dados $x_1,\dots,x_n$ puntos (donde evaluaremos el polinomio) que toman valores $y_1,\dots,y_n$, existe un único polinomio que *interpola* a estos datos en estos puntos. Es decir, existe un polinomio $p$ de grado a lo más $n-1$ de la forma 

$$p(x)=c_0+c_1x+\cdots+c_{n-1}x^{n-1}$$

tal que en cada $x_i$, $p(x_i)=y_i$. Veamos que podemos expresar esto como un sistema de ecuaciones lineales

$$
\begin{bmatrix}
1 & x_1 & {x_1}^2 &        & {x_1}^{n-1}\\
1 & x_2 & {x_2}^2 & \cdots & {x_2}^{n-1}\\
1 & x_3 & {x_3}^2 &        & {x_3}^{n-1}\\
  & \vdots &      &        & \vdots     \\
1 & x_n & {x_n}^2 &        & {x_n}^{n-1}
\end{bmatrix}
\begin{bmatrix}
c_0\\
c_1\\
c_2\\
\vdots\\ 
c_{m-1}
\end{bmatrix}=
\begin{bmatrix}
y_0\\
y_1\\
y_2\\
\vdots\\
y_{m-1}
\end{bmatrix}
$$
> **Entregable 5.** Completa el código en `main.py`

> **Entregable 6.** Añade una gráfica de la interpolación de un polinomio a $\sin(x)$ en el intervalo $[0,2\pi]$ con $100$ puntos. Recibe 2 puntos extras adicionales en la práctica de tu elección si eres capaz de generar un gif que muestre como la interpolación pasa de $2$ puntos a $100$. Para ello puedes consultar este [link](https://matplotlib.org/stable/users/explain/animations/animations.html)
