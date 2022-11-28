# exercícios python
# william pena forte 11-11-2022
# exemplo operador atiritimetico

# ordem de procedencia, nada mais e doque a ordem em que o computador ira realziar as operações matematicas.
#1 () parentese
#2 ** potenciação
#3 *  /  //  %
#4 + e 2

#1 exemplo de ordens de programação
# 5+3*2

print('(5+3)*2 e', (5+3)*2)
print('-' *20)
print('5+(3*2) e', 5+(3*2))
print('-' *20)
print('(3*2)+5 e', (3*2)+5)
print('-' *20)

# exemplo de como multiplicar informações na tela por comando
nome = input('qual seu nome? ')
print('prazer em te conhecer {:20}!'.format(nome)) # repare no espaços
print('prazer em te conhecer {:>20}!'.format(nome)) # repare no espaços agora alinha a direita
print('prazer em te conhecer {:-^20}!'.format(nome)) # repare no espaços agora alinha a direita
print('prazer em te conhecer {:-^20}!'.format(nome)) # repare no espaços agora alinha a direita
print('prazer em te conhecer {:^20}!'.format(nome))

vazio = ''
print ('{:-^100}'.format(vazio))

n1 = int(input('digite um valor'))
n2 = int(input('digiti outro valor'))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

vazio = ''
print ('{:-^100}'.format(vazio))

print('a soma e {} , o produto e {} , e a divisao e {} , '.format(s,m,d)) # aqui a linha sera quebrada
print('divisao inteira {} , e potencia {} , '.format(di,e))

vazio = ''
print ('{:-^100}'.format(vazio))

print('a soma e {} , o produto e {} , e a divisao e {}, '.format(s,m,d), end=' ')# desta vez o print nao quebrara a linha
print('divisao inteira {} , e potencia {} , '.format(di,e))

vazio = ''
print ('{:-^100}'.format(vazio))

print('a soma e {} ,\n o produto e {} ,\n e a divisao e {},\n '.format(s,m,d))# quebrando linhas
print('divisao inteira {} ,\n e potencia {} ,\n '.format(di,e))

vazio = ''
print ('{:-^100}'.format(vazio))

print('a soma e {} ,\n o produto e {} ,\n e a divisao e {},\n '.format(s,m,d), end=' ')# quebrando linhas tudo junto
print('divisao inteira {} ,\n e potencia {} ,\n '.format(di,e))



