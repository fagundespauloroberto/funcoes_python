
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
    try:
        with open("lista_de_palavras.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip() # Remove espaços e \n
                if maiusculas_e_minusculas:
                    if palavra == item:
                        return True
                else:
                    if palavra.lower() == item.lower():
                        return True
        return False
    except FileNotFoundError:
        return False

def palavra_tem_caractere(palavra, lista_caracteres):
    for char in palavra:
        if char in lista_caracteres:
            return True
    return False

def calcular_complexidade(palavra):
    pontos = 0
    if palavra_tem_caractere(palavra, MINUSCULAS): 
        pontos += 1
    if palavra_tem_caractere(palavra, MAIUSCULAS): 
        pontos += 1
    if palavra_tem_caractere(palavra, DIGITOS):    
        pontos += 1
    if palavra_tem_caractere(palavra, ESPECIAIS):  
        pontos += 1
    return pontos

def validar_senha(senha, comprimento_min=10, comprimento_forte=16):
    """Valida a senha e retorna a força de 0 a 5."""
    
    # 1. Verificar se a senha é uma palavra comum ou senha comum
    palavra_lista = procurar_palavra(senha, "lista_de_palavras.txt")
    senha_comum = procurar_palavra(senha, "senhas_mais_comuns.txt")
    if palavra_lista:
        print("Aviso: A senha é uma palavra do dicionário e não é segura!")
        return 0
    elif senha_comum:
        print("Aviso: A senha é comumente usada e não é segura!")
        return 0
    else:        # A senha não é uma palavra comum ou senha comum. 
                 # Continuamos com a validação...
        # 2. Verificar Comprimento
        tamanho = len(senha)
        if tamanho < comprimento_min:
            print(f"Aviso: Senha muito curta (mínimo {comprimento_min} caracteres).")
            return 1

        # 3. Calcular Complexidade
        complexidade = calcular_complexidade(senha)
        
        # Lógica de Força Final:
        # Se for maior que o comprimento forte e tiver complexidade 4 -> Força 5
        if tamanho >= comprimento_forte and complexidade == 4:
            print("Senha Excelente!")
            return 5
        elif complexidade >= 3:
            print("Senha Boa.")
            return 4
        elif complexidade >= 2:
            print("Senha Razoável.")
            return 3
        else:
            print("Senha Fraca.")
            return 2

def main():
    print("--- VALIDADOR DE SENHAS ---")
    while True:
        senha = input("\nDigite uma senha para testar (ou 'q' para sair): ")
        
        if senha.lower() == 'q':
            print("Programa encerrado.")
            break
        
        forca = validar_senha(senha)
        print(f"Avaliação final: {forca}/5")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    main()