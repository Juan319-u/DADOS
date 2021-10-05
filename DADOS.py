import random
import matplotlib.pyplot as plt
y=int(input("ingrese los dados que desee "))
x=int(input("ingrese los casos posibles "))
numeros={}
u=0
d=0
t=0
c=0
cc=0
s=0
for i in range(y*x):
    valor=random.randint(1, 6)
    if valor==1:
        u=u+1
    if valor==2:
        d=d+1
    if valor==3:
        t=t+1
    if valor==4:
        c=c+1
    if valor==5:
        cc=cc+1
    if valor==6:
        s=s+1
numeros[i]=valor
i=+1 

total=u+d+t+c+cc+s
probapar=((d+c+s)/total)*100
probaimpar=((u+t+cc)/total)*100

print(numeros.values())
print("este es la cantidad de 1 que hay ",u)
print("este es la cantidad de 2 que hay ",d)
print("este es la cantidad de 3 que hay ",t)
print("este es la cantidad de 4 que hay ",c)
print("este es la cantidad de 5 que hay ",cc)
print("este es la cantidad de 6 que hay ",s)
print("el total de resultados es ",total)
print("la probabilidad de sacar par es",probapar,"%")
print("la probabilidad de sacar impar es",probaimpar,"%")
hist=plt.hist(numeros.values())
