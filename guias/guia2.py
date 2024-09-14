import numpy as np

#EJ7

#a)
p = 1e34
q = 1

#print(p+q-p)

#b)

p= 100
q=1e-15

# print((p+q)+q)
# print(2*q+p)
# print(((p+q)+q)+q)
# print(3*q+p)

#dan todos iguales ya que q es muy chico y no llega a sumar en las cifras significativas

#c)
#print(0.1+0.2)
#problema ya que el 0.1 en bianrio es periodica entonces tiene ese error

#d)
#print(0.1+0.4)

#e)
#print(1e-323)

#f)
#print(1e-324)
#es un underflow 

#g)

e = np.finfo(float).eps
# print(e)

#print(e/2)

#h)
#print((1+e/2)+e/2)
#e es el numero mas chico que se le puede sumar a 1 y provocar un cambio, como sumo e/2 no cambia nada

#i)
#print(1+(e/2+e/2))
#ahora si cambia ya que primero hago la suma de los e/2 lo que da como resultado e y luego suma 1

#j)
#print(((1+e/2)+e/2)-1)
#se va a 0 por motivo en h

#k)
#print(1+(e/2+e/2)-1)
#obtenemos epsilon

#l)
# for i in range(1,26):
#     print(np.sin((10**i)*np.pi))

#tendria que dar 0 pero como pi no es numero de maquina dan esos errores

#m)
# for i in range(1,26):
#     print(np.sin(np.pi/2 + (10**i)*np.pi))

#al principio da 1 porq se multiplica pi por un numero no tan grande luego comienzan los errores por numeros de punto flotante

#EJ8

import numpy as np

n = 7
s1 = np.float32(0)
for i in range(1,10**n+1):
   s1 += np.float32(1/i)

print("suma = ", s1)

s2 = np.float32(0)
for i in range(1,2*10**n+1):
    s2 += np.float32(1/i)

print("suma = ", s2)


##da numeros iguales

#de esta forma lo mejoro

import numpy as np

n = 7
s1 = np.float32(0)
for i in range(1,10**n+1):
   s1 += np.float32(1/((10**7)+1-i))

print("suma = ", s1)

s2 = np.float32(0)
for i in range(1,2*10**n+1):
    s2 += np.float32(1/((2*10**7)+1-i))

print("suma = ", s2)