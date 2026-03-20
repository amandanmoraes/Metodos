import numpy as np
import math 
import matplotlib.pyplot as plt

# Dados Iniciais 
x = 1
n = 6
u = math.exp(1)


# Fórmula Geral ( Série de Maclaurin )
def ex(x,n):
    return x**n/math.factorial(n)
na = 6
Eppara = (1/2)*10**(2-na)

# Pré-alocação 
soma= 0
estimativa = []
contador = []
EPT = []
EPEST = [100]
v_old = 0
Ept = 100
Epest = 100
i = 0

while (Ept > Eppara and Epest > Eppara):
    print ( Ept )
        
    soma = soma + ex(x,i)
    v_new = soma
    Ept = abs((u - soma)/u)*100
        
    if i > 0:
        Epest = abs((v_new - v_old)/v_new)*100
        EPEST.append(Epest)
            
    #Atualização
    v_old = v_new
    i = i + 1

    EPT.append(Ept)
        
    estimativa.append(soma)
    contador.append(i)
    
plt.figure()
plt.plot(contador,estimativa,'or', label = "$e^x$")
plt.legend()
plt.xlabel("Número de Termos")
plt.ylabel("Estimativa")
plt.grid()

plt.figure()
plt.plot(contador,EPT,'ok',label="$E_{pt}$")
plt.plot(contador,EPEST,'og',label="$E_{pest}$")
plt.legend()
plt.xlabel("Número de Termos")
plt.ylabel("$E_{pt}$ ou $E_{pest}$ (%)")
plt.grid()
plt.show()