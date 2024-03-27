print ("Gisella")

numero = 13
nome = "Gisella linda"
booleano = True

numero_real = 13.0

resposta = ( 2 < 4 )or ( 4 == 5)

# ordem de execução em Python segue este fluxo geral:
#1.Processamento de linhas de comando e importações.
#2.Definição de funções e classes.
#3.Execução do código principal no escopo global.
#4.Chamadas de funções, com a execução do código dentro delas.
#5.Execução de chamadas de função recursivas, se houver.
#6.Aplicação de instruções de controle de fluxo, como if, elif, else, for, while.
#7.Tratamento de exceções, se ocorrerem.
#8.Finalização da execução, a menos que haja mais código a ser executado além do final do programa.





## Ordem de Precedência dos Operadores Lógicos:

#A ordem de precedência dos operadores lógicos em Python é a seguinte:

#1. Parênteses ( )
#2. Not (not)
#3. And (and)
#4. Or (or)

## Exemplo de Modificação da Ordem das Operações Lógicas:



# Aqui a expressão será avaliada como True, porque 'False and True' é False, e 'True or False' é True.
resposta_modificada = (2 < 4) and (4 == 5) or (6 > 3)

print(resposta_modificada)  # Output: True
