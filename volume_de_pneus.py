'''
Escreva um programa que receba do usuÃ¡rio informaÃ§Ãµes sobre um pneu, em seguida calcule e exiba o volume do pneu. 
Registre tambÃ©m os dados em um arquivo de texto (log).
Solicite ao usuÃ¡rio a largura do pneu em mm.              OK
Solicite ao usuÃ¡rio a proporÃ§Ã£o.                          OK 
Solicite ao usuÃ¡rio o diÃ¢metro da roda em polegadas.      OK
Calcule e exiba o volume do pneu com duas casas decimais. OK
Registre as informaÃ§Ãµes em um arquivo de texto (log).     OK
data atual (NÃƒO inclua a hora)                            OK

largura do pneu                                              
proporÃ§Ã£o do pneu
diÃ¢metro da roda
volume do pneu (arredondado para duas casas decimais)
'''
import math
from datetime import datetime
import os

w = int(input('Digite a largura do pneu em mm (por exemplo: 205): 185 '))
a = int(input('Digite a proporÃ§Ã£o do pneu (por exemplo: 60): 50 '))
d = int(input('Digite o diÃ¢metro da roda em polegadas (por exemplo: 15): 14 '))

pi = math.pi    
v = (pi * (w**2) * a * (w * a + 2540 * d)) / (10**10)
print(f'O volume aproximado Ã© de  {v:.2f} litros')

agora = datetime.now()
data = agora.strftime("%d/%m/%Y") #formatando a data
print(f'Data {data}') #confirmando a data apresentada

with open("volume_pneu.txt", "a") as arquivo:
    linha = f"ParÃ¢metros: Largura={w}, ProporÃ§Ã£o={a}, DiÃ¢metro={d}, Data={data} | Resultado: {v:.2f}\n"
    arquivo.write(linha)
    print('Registro gerado com sucesso.')
    
caminho_atual = os.getcwd() #para apresentar o caminho do arquivo, jÃ¡ que nÃ£o definimos o mesmo...
print(f"O seu arquivo de log estÃ¡ salvo em: {caminho_atual}")