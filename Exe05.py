"""
Exercicios seção 05
"""

"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior

# Entrada de dados
print("QUAL NÚMERO É MAIOR?")

num1 = str(input("Primeiro Número ?"))
num2 = str(input("Segundo Número ?"))

if num1 > num2:
    print('Primeiro Número é Maior')
elif num1 == num2:
    print('Iguais')
else:
    print('Segundo Número é Maior')


"""
"""
2 - Leia um número fornecido pelo usuário. Se essse número for positivo, calcule a 
raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.


# Entrada de dados
print("ESSE NÚMERO TEM RAIZ?")

num1 = float(input(" Insira um número ?"))
raiz = float(num1) ** 0.5

if num1 >= 0:
    print(f' A Raiz quadrada de {num1} é {raiz}')
else:
    print('Número é inválido')
        
"""
"""
3 - Leia um número real. Se o número for positivo impirma a raiz quadrada. Do contrário, imprima o numero ao quadrado.

num1 = -20
raiz = (num1) ** 0.5
quadrado = (num1) ** 2
if num1 >= 0:
    print(f'A Raiz quadrada de {num1} é {raiz}')
else:
    print(f'Ao quadrado de {num1} é {quadrado}')

"""
"""
4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    1 - O número digitado ao quadrado.
    2 - A raiz quadrada do número digitado.
    
    # Entrada de dados
num1 = float(input('Insira um Número'))
raiz = (num1) ** 0.5
quadrado = (num1) ** 2
if num1 >= 0:
    print(f'A Raiz quadrada de {num1} é {raiz}', f'\n E o quadrado de {num1} é {quadrado}')
else:
    print(f' O {num1} é inválido')

"""
"""
5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.


# Entrada de dados
num1 = int(input('Insira um Número inteiro'))

if (num1%2) == 0 :
    print(f'O número {num1} é Par')
else:
    print(f'O número {num1} é Ímpar')
    
"""
"""
6 - Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença
existente entre ambos.

# Entrada de dados
num1 = int(input('Insira um Número inteiro'))
num2 = int(input('Insira um Número inteiro'))


if num1 > num2:
    num3 = num1 - num2
    print(f'{num1} é maior \n e a diferença entre eles é {num3}')
else:
    num3 = num2 - num1
    print(f' {num2} é maior \n e a diferença entre eles é {num3}')

"""
"""

8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas
notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor 
válido, este fato deve ser iformado ao usuário e o programa termina


# Entrada de dados
num1 = float(input('Insira a Primeira Nota'))
num2 = float(input('Insira a Segunda Nota'))


if (0 < num1 < 10) and (0 < num2 <10) :
    num3 = ((num1 + num2) / 2)
    print(f'A média entre as notas {num1} e {num2} é \n igual a :{num3}')
else:
    print(f' Nota não é válida ')

"""
"""
7 - faça um programa que que receba dois números e mostre o maior. Se por acaso os dois números forem iguais, 
imprima a mensagem Números Iguas.

# Entrada de dados
print("QUAL NÚMERO É MAIOR?")

num1 = str(input("Primeiro Número ?"))
num2 = str(input("Segundo Número ?"))

if num1 > num2:
    print('Primeiro Número é Maior')
elif num1 == num2:
    print('Iguais')
else:
    print('Segundo Número é Maior')
    
"""
"""
9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário
imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

# Entrada de dados
print('Simulação de Empréstimo')
salario = float(input('Insira seu Salário'))
prestação = float(input('Insira a Prestação'))

if prestação > salario * 0.2:
    print('Empréstimo não concedido')
else:
    print(f'Empréstimo concedido ')

"""
"""
10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas( onde h corresponde à altura):
    * Homens:(72.7 * h) - 58
    * Mulheres: (62.1 * h) - 44.7
    
    # Entrada de dados
print('Qual seu peso Ideal')
altura = float(input('Insira sua Altura em metros'))
sexo = int(input('Insira e seu Genero, 1 para homem e 2 para mulher'))
homem = 1
mulher = 2

if sexo == homem:
    peso_ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é  {peso_ideal}')
elif sexo == mulher:
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é  {peso_ideal}')
else:
    print(f'Genêro Inválido')
    
"""
"""
11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus
algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2 + 5 + 1). Se o numero lido não for maior do que zero,
o programa terminará com o mensagem "Número inválido".

num = input("Digite um número: ")
if num.isdecimal() and int(num) > 0:
    print(f"A soma dos dígitos de {num} é {sum(map(int, num))}")
else:
    print("Valor inválido")
    
"""
"""
12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positi-
vo, calcular o logaritmo deste numero. 

# Entrada de dados
print("QUAl é o LOG?")

n = int(input("Primeiro Número: "))
import math
if n > 0:
    print(f" o Log de {n} é {math.log( n,10 )}")
else:
    print('Número inválido')

"""
"""
13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a
terceira tem peso 2. Ao final, mostras a média do aluno e indicar se o aluno for aprovado ou reprovado. A nota para
aprovação deve ser igual ou superior a 60 pontos.

# Entrada de dados
print('Aluno aprovado ou não')
p1 = float(input('Insira a Nota da prova 1: '))
p2 = float(input('Insira a Nota da prova 2: '))
p3 = float(input('Insira a Nota da prova 3: '))
media = (((p1 * 1) + (p2 * 1) + (p3 * 2)) / 4)
if  media >= 60:
    print(f" A Média do aluno é {media} e está aprovado")
else:
    print(f" A Média do aluno é {media} e não está aprovado")
    
"""
"""
14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, 
respectivamente, a um trabalho de labóratorio, a uma avaliação semestral e a um exame final. A média das três notas 
mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2 ; Avaliação Semestral: 3; Exame Final: 5.
De acordo comm o resultado, mostre na tela se o aluno está reprovado( média entre 0 e 2,9),de recuperação 
(entre 3 e 4,9) ou se foi aprovado. Faça toas as verificações necessárias.

# Entrada de dados
print('Aluno aprovado ou não')
tl = float(input('Insira a Nota da prova 1: '))
avs = float(input('Insira a Nota da prova 2: '))
ef = float(input('Insira a Nota da prova 3: '))
media = (((tl * 2) + (avs * 3) + (ef * 5)) / 10)


if  (5 <= media <= 10) and (0.0 <= tl, avs, ef <= 10):
    print(f" A Média Final do aluno é {media} e está Aprovado")

elif (3 <= media <= 4.9) and (0.0 <= tl, avs, ef <= 10):
    print(f" A Média do aluno é {media} e está de Recuperação")

elif (0 <= media <= 2.9) and (0.0 <= tl, avs, ef <= 10):
    print(f" A Média do aluno é {media} e está Reprovado")

else:
    print(f" Valores incorretos")
 
"""
"""
15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente 
a este número. Isto é, domingo se 1, segunda-feria se 2, e assim por diante. 

 Entrada de dados
print('Advinhe o dia da semana com um numero')
list = [' ','domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']

dia = int(input('Digite um Número de 1 a 7 e veja o dia da semana:  '))

print(f'O dia da semana é {list[dia]}')

"""
"""
16 -  Usando switch, escreva um programa que leia um inteiro enre 1 e 12 e imprima o mês correspondete a este numero.
Isto é, janeiro se 1 , fevereiro se 2 e assim por diante.

 Entrada de dados
print('Advinhe o dia da semana com um numero')
list = [' ','janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho'....]

dia = int(input('Digite um Número de 1 a 7 e veja o dia da semana:  '))

print(f'O dia da semana é {list[dia]}')

"""
"""
17 - Faça um programa que calcule e mostre a área de um trapézio. sabe-se que:

A = ( (basemaior + basemenor) * altura)) / 2

# Entrada de dados
print('Calcule a Área do Trápezio')
basemaior = float(input('Insira a Base Maior em cm: '))
basemenor = float(input('Insira a Base Menor em cm: '))
altura = float(input('Insira a Altura cm: '))
area = (((basemaior + basemenor) * (altura)) / 2)


if  (0.0 < basemaior, basemenor, altura):
    print(f" A Área do Trapézio é {area}cm")
else:
    print(f" Valores incorretos")

"""

"""
18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas ( as básicas, por exemplo).
O usuário escolhe uma das opções e o seu preograma então pede dois valores numéricos e realiza a operação, mostrando 
o resultado e saindo.


# Entrada de dados
print('Escolha uma das operações matemáticas soma ,subtração, multiplicação, divisão')
print('1 para soma , \n2 para  subtração ,\n3 para multiplicação,\n4 para divisão')
x = int(input('QUAL É A SUA ESCOLHA: '))


if  x == 1 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z + y
     print(f" A soma é igual a  {totalsoma}")

elif x == 2 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z - y
     print(f" A subtração é igual a  {totalsoma}")

elif x == 3 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z * y
     print(f" A Multiplicação é igual a  {totalsoma}")

elif x == 4 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z / y
     print(f" A divisão é igual a  {totalsoma}")

else:
    print(f" Escolha incorreta")
    
"""
"""

19 - Faça um preograma para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente
pelos dois.

# Entrada de dados
print('Será que é divisível por 3 ou 5')
x = int(input('Insira um valor inteiro: '))

if (x%3) == 0:
    print(f'Este número é divisível por 3')
elif (x%5) == 0 :
    print(f'Este número é divisível por 5')
else:
    print(f" Não é divisível")

"""
"""

20 - Dados três valores, A,B,C verificar se eles podem ser vaores dos lados de um triângulo e, se forem, se é um 
trinângulo escaleno,equilátero ou isóscele, considerando os seguintes conceitos:
* O comprimento de cada lado de um triângulo é menos do que a soma dos outros dois lados.
* Chama-se equilátero o triangulo que tem três lados iguais
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o trinângulo que tem os três lados diferentes.

# Entrada de dados
print('Vamos descobrir qual triangulo temos através so das medidas.')
a = int(input('Insira um valor inteiro para um lado do triangulo: '))
b = int(input('Insira um valor inteiro para um lado do triangulo: '))
c = int(input('Insira um valor inteiro para um lado do triangulo: '))


if (a < (b + c)) and (b < (a + c)) and (c < (a + b))  :
    print(f'Isto é um Triângulo')
    if  a == b == c:
            print(f'E como os lados {a} , {b} e {c}  são iguais temos um Trinângulo Equilátero')
    elif a == b or a == c or b == c:
            print(f'E como há dois lado iguais sendo eles {a} , {b} e {c} temos um Trinângulo Isósceles')
    else :
            print(f'E como todos os lados são diferentes sendo eles {a} , {b} e {c} temos um Trinângulo Escaleno')
else:
    print(f" Não é um Triângulo")

"""
"""
21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. 
Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números ( maior pelo menor)
3 - Produto entre 2 números.
4 - Divisão entre 2 números ( o denominador não pode ser zero).
 

# Entrada de dados
print('Escolha uma das OPÇÔES?')
print('1 - Soma de 2 números. \n2 - Diferença entre 2 números ( maior pelo menor). \n3 - Produto entre 2 números.\n4 - Divisão entre 2 números ( o denominador não pode ser zero).')
x = int(input('QUAL É A SUA ESCOLHA: '))


if  x == 1 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z + y
     print(f" A soma é igual a  {totalsoma}")

elif x == 2 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     if z > y :
        totalsoma = z - y
        print(f" A subtração é igual a  {totalsoma}")
     elif y > z:
        totalsoma = y - z
        print(f" A subtração é igual a  {totalsoma}")
     else:
        print(f" Opção nao suportada")
elif x == 3 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     totalsoma = z * y
     print(f" A Multiplicação é igual a  {totalsoma}")

elif x == 4 :
     z = int(input('Insira um valor: '))
     y = int(input('Insira um valor: '))
     if (y != 0) :
        totalsoma = z / y
        print(f" A divisão é igual a  {totalsoma}")
     elif (z != 0):
        totalsoma = y / z
        print(f" A divisão é igual a {totalsoma}")
     else:
         print(f" Opção nao suportada")

"""