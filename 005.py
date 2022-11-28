# exercícios python
# william pena forte 11-11-2022

# fazer um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
# exp numero 8 -- antecessor 7 , num 8 , sucessor 9

a = int(input('digiti um numero: '))
ant = a - 1
suc = a + 1
print('analisando o valor e {} , seu antecessor e {} , e o sucessor e {} '.format(a,ant,suc))

#pulando linha
v = ' '
print ('{:^100}'.format(v))

a = int(input('digiti um numero: '))
#ant = a - 1
#suc = a + 1
print('analisando o valor e {} , seu antecessor e {} , e o sucessor e {} '.format(a, (a-1),(a+1)))
