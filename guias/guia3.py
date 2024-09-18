import numpy as np

#EJ 2

A = np.array([[1,-1,0,1],[0,1,4,0],[2,-1,0,-2],[-3,3,0,-1]])
b = np.array([1,-7,-5,1])

#print(np.linalg.solve(A,b))

#EJ 3

#resolucion con triangular inferior:

#a
def sustitucion_hacia_adelante (L,b):
    res = np.array([])
    
    for i in range (np.shape(L)[0]):
        num = b[i]
        den = L[i,i]
        for j in range(i):
            num -= L[i,j]*res[j]
        
        x_i = num/den
        res = np.append(res, x_i)
        
    
    return res

L = np.array([[1,0,0,0],[0,1,0,0],[2,1,1,0],[-3,0,0,1]])
b = np.array([1,-7,-5,1])

y = sustitucion_hacia_adelante(L, b)

#b

def sustitucion_hacia_atras(U,y):
    res = np.array([])
    n = np.shape(U)[0]
    
    for i in range (n):
        num = y[n-1-i]
        den = U[n-1-i,n-1-i]

        for j in range(i):            
            num -= U[n-1-i,n-1-j]*res[len(res)-1-j]
                    
        x_i = num/den

        res = np.insert(res, 0,x_i)
        
    
    return res

U = np.array([[1,-1,0,1],[0,1,4,0],[0,0,-4,-4],[0,0,0,2]])
#print(sustitucion_hacia_atras(U,y))

#EJ 4

#a)
#calcularLU

def calcularLU(A):
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR
    L = np.eye(n) #inciamos L de nxn

    matricesPermutacion=[]

    

    #Gaussian Elimination
    for i in range(n):
        if Ac[i,i]==0:
            
            
            listaDePivotes:list[tuple] = []
            for j in range(i+1,n):
                listaDePivotes.append((Ac[j,i],j))   #listaDePivotes.append((elemento,indice)), tupla = (elemento,indice)

            

            newPivoteIndice= listaDePivotes[0]
            
            for k in range(len(listaDePivotes)-1):
                    
                if newPivoteIndice[0]<= listaDePivotes[k][0]:
                    newPivoteIndice = listaDePivotes[k]
                
            #ahora resta crear una identidad con las filas intercambiadas por los indices newPivote[]


            identidad = np.eye(n)
            permutacion = np.eye(n)     #la transformo mas abajo, arranco con la Identidad
            permutacionFila1 = identidad[i]
            permutacionFila2 = identidad[newPivoteIndice[1]]
            permutacion[i] = permutacionFila2
            permutacion[newPivoteIndice[1]]=permutacionFila1 
            matricesPermutacion.append(permutacion) #estaran en la fila en un orden inverso al propuesto para conseguir P



            Ac= permutacion @ Ac
            
            for k in range (i):
                L[0:,k] = (permutacion @ L[0:,k])
                 

        for j in range(i+1, n):
            factor = Ac[j,i] / Ac[i,i]#aca va q multiplico entre las matrices para q de 0.
            L[j,i] = factor # guardamos el factor en la matriz L 
            Ac[j,i:] = Ac[j,i:]  - factor*Ac[i,i:]
            


    if(len(matricesPermutacion)>=1):
        P=multiplicarPermutaciones(matricesPermutacion)
    else:
        P = np.eye(n)
            
    U = np.triu(Ac)
    
    return L, U, P

def multiplicarPermutaciones(matricesPermutaciones:list):
    P=matricesPermutaciones[len(matricesPermutaciones)-1]
    for i in range(len(matricesPermutaciones)-2,-1,-1):         #el menos 1 del segundo item es porque es -1 exclusive
        Pnmenos1 = matricesPermutaciones[i]
        P = P @ Pnmenos1

    return P

#b)

L, U, P = calcularLU(A)
y = sustitucion_hacia_adelante(L,b)
x = sustitucion_hacia_atras(U,y)
#print(x)