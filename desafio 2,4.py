import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
#print(f"Current Year -> {year}")

dia = input ('Qual o dia do seu nascimento?')
mes = input ('Qual o mes do seu nascimento?')
ano = input ('Qual o ano do seu nascimento?')

#ano = int(ano)

ano_atual = int(year)
idade = (ano_atual - ano)

print ('Você nasceu em',dia,'de',mes,'de',ano,'\n É tem',idade,'anos de idade')
