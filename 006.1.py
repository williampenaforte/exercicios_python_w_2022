# exercícios python
# william pena forte 11-11-2022

# fazer um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
# exp numero 8 -- antecessor 7 , num 8 , sucessor 9

# desenvolva um programa que leia as mduas notas de um aluno, calcule e mostre sua media.

#tela de boas vindas
print('Calculadora de media escolar.')
print('A media e 7:')

#faz pular linha
v = ' '
print('{:100}'.format(v))

#coleta de dados
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))

#aplica formula
r = (n1 + n2) / 2

#faz pular linha
v = ' '
print('{:100}'.format(v))

#tomada de decisão
if r > 7:
    print('Aluno Aprovado')
    #print('A primeira nota do aluno foi {},\n A segunda nota do aluno foi {},\n A sua media e {}'.format(n1,n2,r))
else:
    print('Aluno Reprovado')