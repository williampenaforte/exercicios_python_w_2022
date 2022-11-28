# exercicios py
# william pena
# escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

medida = float(input('Digite uma distância em  metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}M correponde a {:.0f}CM e {:.0f}MM'.format(medida, cm, mm))

