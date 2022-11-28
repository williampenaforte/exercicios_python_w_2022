# exercícios python
# william pena forte 11-11-2022

# fazer um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.

# desenvolva um programa que leia as mduas notas de um aluno, calcule e mostre sua media.
n1 = float(input('Qual a primeira nota do aluno? '))
n2 = float(input('Qual a segunda nota do aluno? '))

r = (n1 + n2) / 2

print('A primeira nota do aluno foi {:.1f},\n A segunda nota do aluno foi {:.1f},\n A sua media e {:.1f}'.format(n1,n2,r))
