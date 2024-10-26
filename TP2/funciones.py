### Metodo de la potencia

import numpy as np

def metodo_potencia (A):
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
    
    for i in range (n):                                 #para calcular el autovalor hago la division de cada coordenada de la multiplicacion de A por v y v. Y luego saco el promedio
        autovals[i] = product[i]/v[i]
    
    autovalor = np.mean(autovals)    
    #autovalor = product[1]/v[1]
    
    return autovalor

A = np.array([[2,3],[2,1]]) 
print(metodo_potencia(A))