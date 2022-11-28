dia_str = input ('Qual o dia do seu nascimento?')
mes_str = input ('Qual o mes do seu nascimento?')
ano_str = input ('Qual o ano do seu nascimento?')

ano_int = int(ano_str)

ano_atual = 2022
idade = ano_atual - ano

print ('Você nasceu em',dia,'de',mes,'de',ano,'/n É tem',idade,'de idade')
