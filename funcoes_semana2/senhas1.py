
#Fornece o loop de entrada do usuário. O loop solicita ao usuário uma senha para teste. 
#Se a senha for qualquer coisa diferente de "q" ou "Q", chame a função validar_senha e informe os resultados ao usuário. 
#Se o usuário digitar "q" ou "Q", saia do programa.

'''
procurar_palavra	
*Parâmetros*
palavra,
nome_do_arquivo,
maiusculas_e_minusculas

*Tipo de Retorno*
Booleano (True ou False)	
Esta função lê um arquivo (informado pelo parâmetro nome_do_arquivo), em que cada linha contém uma única palavra.
Se a palavra passada no parâmetro palavra corresponder a uma palavra no arquivo, a função retornará True; caso contrário, retornará False.
Se o parâmetro maiusculas_e_minusculas for True, a comparação será feita com distinção entre maiúsculas e minúsculas.
Se for False, a comparação será feita sem distinção entre maiúsculas e minúsculas (comportamento padrão).
Por padrão, o parâmetro maiusculas_e_minusculas deve ser False

*palavra_tem_caractere*
*Parâmetros*
palavra,
lista_caracteres

*Tipo de Retorno*
Booleano (True ou False)	
Esta função percorre cada caractere da string passada no parâmetro palavra para verificar se ele está presente na lista de caracteres informada no parâmetro lista_caracteres.
Se algum caractere da palavra estiver na lista de caracteres, a função retornará True.
Se nenhum caractere da palavra estiver na lista, a função retornará False.

*calcular_complexidade*	
*Parâmetros*
palavra

*Tipo de Retorno*
Inteiro	Esta função cria um valor numérico que representa a complexidade da senha com base nos tipos de caracteres que o parâmetro palavra contém.
Um ponto de complexidade é atribuído para cada tipo de caractere presente na palavra.
A função chama palavra_tem_caractere para verificar cada um dos quatro tipos de caracteres:
Minúscula
Maiúscula
Dígitos
Especial
Se a palavra contiver esse tipo de caractere, um ponto será adicionado à classificação de complexidade. Como existem quatro tipos de caracteres, a classificação de complexidade variará de 0 a 4.
O valor 0 será retornado apenas se a palavra estiver vazia ou contiver apenas caracteres que não pertençam a nenhuma das listas acima.

*validar_senha*	
*Parâmetros*
senha,
comprimento_min,
comprimento_forte

*Tipo de Retorno*
Inteiro	A função validar_senha verifica os requisitos de comprimento, chama calcular_complexidade para calcular a complexidade da senha e então determina a força final com base nos requisitos do usuário.
Ela deve exibir as mensagens definidas nos requisitos e retornar a força da senha como um número de 0 a 5.
O parâmetro comprimento_min deve ter um valor padrão de 10. O parâmetro comprimento_forte deve ter um valor padrão de 16.
main		
Fornece o loop de entrada do usuário. O loop solicita ao usuário uma senha para teste. Se a senha for qualquer coisa diferente de "q" ou "Q", chame a função validar_senha e informe os resultados ao usuário. Se o usuário digitar "q" ou "Q", saia do programa.'''

from ast import main

#CONSTANTES
MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas=False):
    pass

def palavra_tem_caractere(palavra, lista_caracteres):
    pass

def calcular_complexidade(palavra):
    pass

def validar_senha(senha, comprimento_min=10, comprimento_forte=16):
    pass

def main():
    print("Seja bem-vindo ao Validador de Senhas!")
    print("--- VALIDADOR DE SENHAS ---")
    while True:
        senha = input("Digite sua senha escolhida para validação (use 'Q' ou 'q' para sair): ")
        
        if senha.lower() == 'q':
            print("Programa encerrado.")
            break
        
        #forca = validar_senha()
        print(f"Sua senha é {senha}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    main()