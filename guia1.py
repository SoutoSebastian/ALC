import numpy as np
import matplotlib.pyplot  as plt

#########EJ 3
#Vectores

v = np.array([1,2,3,-1])
w = np.array([2,3,0,5])

# print(v+w)
# print(2*v)
# print(v**2)


#Matrices

A = np.array([[1,2,3,4,5],[0,1,2,3,4],[2,3,4,5,6],[0,0,1,2,3],[0,0,0,0,1]])
#print(A)
#print(A[0:2, 3:5])
#print(A[:2, 3:])

#print(A[ [ 0 , 2 , 4 ] , : ])
ind = np.array( [ 0 , 2 , 4 ] )
#print(A[ ind , ind ])
#print(A[ ind , ind [ : , None ] ])

#Numeros complejos

# print(1j*1j)
#print((1+2j)*1j)

#########EJ 4
# A = np.array([[1,1,1],[4,2,1],[9,3,1]])
# b = np.array([1,2,0])
# x = np.linalg.solve(A, b)

#print(x)

xx = np.array([1,2,3])
yy = np.array([1,2,0])

x = np.linspace(0,4,100)
f = lambda t:-1.5*t**2+5.5*t-3

# plt.plot(xx,yy,'*')
# plt.plot(x,f(x))
# plt.show()

##EJ 18 calculando determinantes

A = np.array([[1j, 0 ,2+1j],[-1, 1-1j, 0],[2, 0, -1]])

#print(np.linalg.det(A))

#EJ21

#a calcular la traza de una matriz.

def traza(A):
    res = 0
    for i in range (len(A)):
        for j in range (len(A[i])):
            if (i == j):
                res += A[i][j]
                
    return res

#print(traza(np.array([[1,1,1],[4,2,1],[9,3,1]])))

#b Calcular la suma de todos los elementos de una matriz

def suma(A):
    res = 0
    for i in range (len(A)):
        for j in range (len(A[i])):
            res += A[i][j]
            
    return res

#print(suma(np.array([[1,1,1],[4,2,1],[9,3,1]])))

#c Determinar si la sumatoria de elementos positivos es mayor que la sumatoria (en modulo) de los elementos negativos de una matriz.

def posOneg(A):
    res = True
    sumaPos = 0
    sumaNeg = 0
    
    for i in range(len(A)):
        for j in range(len(A)):
            if (A[i][j]>0):
                sumaPos += A[i][j]
            else:
                sumaNeg += A[i][j]
    
    if(sumaPos < (-1*sumaNeg)):
        res = False
        
    return res

#print(posOneg(np.array([[1,1,1],[-4,2,1],[-9,3,1]])))