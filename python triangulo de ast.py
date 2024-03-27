def quadrado(a):
    return a**2
def soma (a,b):
    return a + b
def hipotenusa (cat1, cat2):
    return soma(quadrado(cat1), quadrado(cat2))**(1/2)

h = hipotenusa 

def responda (pfv):
    if pfv == 'quemégisella?' :
        return 'Segundo meus dados ela é o ser mais supremo que ja pisou no planeta.'

def medio(cor):
    if cor == 'azul' :
        return 'arrasou'
    else :
        return 'errou feio seu merda'
        
def completo (cor):
    if cor == 'azul':
        return 'issoooo'
    elif cor == 'marrom':
        return 'minha filha???'
    else :
        return 'NAO'


numeros = [1 ,2 ,3 ,4 ,5]
print (numeros [0])
print (numeros[1])
numeros[0] = 10
print (numeros)

contador = 0
while contador < 10:
    print(contador)
    contador += 1

for i in range (10):
    print(i)

for item in [1, 47, 48, 'd']:
    print (item)
for letra in 'minha string':
    print (letra)
def imprimir_triangulo(linhas):
    for i in range(1, linhas + 1):
        print("*" * i)

#triangulo de asterisco
for i in range(10):
        print("*" * i)
