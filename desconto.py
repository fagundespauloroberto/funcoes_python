# Importa a classe datetime do módulo
# datetime para que ele possa ser usado neste programa.
from datetime import datetime
 
# Chama o método now() para obter a data e hora
# atuais como um objeto datetime do
# sistema operacional do computador.
data_e_hora_atuais = datetime.now()

# Chama o método weekday() para obter o dia da
# semana a partir do objeto data_e_hora_atuais.
dia_da_semana = data_e_hora_atuais.weekday()

desconto = 0.00
subtotal = float(input('Informe o valor de entrada.'))
subtotal += (subtotal * 6 )/100
#if subtotal >= 50 and (dia_da_semana > 2 and dia_da_semana > 5):
if subtotal >= 50:
    desconto = ((subtotal * 10) / 100)
    
# Exibe o dia da semana para o usuário ver.
print(f'dias da semana é {dia_da_semana}')
print(f'valor desconto {desconto}')
print(f'valor do subtotal {subtotal}')

