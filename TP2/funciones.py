### Metodo de la potencia

import numpy as np

def metodo_potencia (A, tol = 0.0001):
    """Recibe una matriz A y una tolerancia. Devuelve el autovalor de mayor modulo y el autovector asociado."""
    n = np.shape(A)[0]
    tol = 0.0001                    #tolerancia pedida para que se deje de ejecutar el while
    dif = tol + 1
    v = np.random.rand(n,1)         #comienzo con un vector random
    
    
    while (dif > tol) :
        v_1 = A@v
        v_1 = v_1 / np.linalg.norm(v_1,2)
        dif =np.linalg.norm((v-v_1),2) 
        v = v_1
        
    autovals = np.zeros(n)
    product = A@v

    #coeficiente de Rayleigh:
    w = A @ v
    autovalor = ((v.T @ w) / (v.T @ v))[0][0]
    
    return autovalor, v

#Ahora hago un metodo de la potencia para Hotelling ( lo unico que cambio es el uso de epsilon)

def metodo_potenciaH (A, e =0.9999):
    """Recibe una matriz A y una tolerancia. Devuelve el autovalor de mayor modulo y el autovector asociado."""
    n = np.shape(A)[0]
    tol = 1 - e                    #tolerancia pedida para que se deje de ejecutar el while
    dif = tol + 1
    v = np.random.rand(n,1)         #comienzo con un vector random
    
    
    while (dif > tol) :
        v_1 = A@v
        v_1 = v_1 / np.linalg.norm(v_1,2)
        dif =np.linalg.norm((v-v_1),2) 
        v = v_1
        
    autovals = np.zeros(n)
    product = A@v

    #coeficiente de Rayleigh:
    w = A @ v
    autovalor = ((v.T @ w) / (v.T @ v))[0][0]
    
    return autovalor, v
