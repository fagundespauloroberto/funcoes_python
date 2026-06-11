'''
Etapa
Comece seu projeto escrevendo e testando a função ler_dicionario.
Crie a função ler_dicionario. Ela deve abrir um arquivo CSV para leitura e usar um csv.reader para ler cada linha e preencher um dicionário composto com o conteúdo do arquivo produtos.csv.
Crie a função main e adicione os seguintes recursos.
Chama a função ler_dicionario e armazene o dicionário retornado na variável dic_produtos.
Exibe o dicionário.
Abre o arquivo pedido.csv para leitura.
Pula a primeira linha do arquivo pedido.csv porque ela contém títulos de coluna.
Usa um loop para ler e processar cada linha do arquivo pedido.csv. Dentro do corpo do loop, seu programa deve fazer o seguinte para cada linha:
Usar o número do produto solicitado para encontrar o item correspondente no dic_produtos.
Exibir o nome do produto, a quantidade solicitada e o preço do produto.
Na parte inferior do seu arquivo recibo.py, adicione uma chamada para a função main. 
Certifique-se de proteger a chamada para main com uma instrução if, conforme ensinado no conteúdo de preparação da semana 3.
'''
# Funcionalidades adicionais
# Apresenta o nome do arquivo que gerou o recibo.
# Apresenta a data limite para devolução dos produtos, que é 30 dias a partir da data do pedido.

import csv
from os import path
from tempfile import mktemp
from datetime import datetime, timedelta

def ler_dicionario(nome_arquivo, indice_chave):
    """Lê um arquivo CSV e retorna um dicionário.
    Parâmetros:
        nome_arquivo: o nome do arquivo CSV a ser lido
        indice_chave: o índice da coluna que deve ser usada como chave no dicionário
    Retorna:
        Um dicionário onde as chaves são os valores da coluna especificada por indice_chave
        e os valores são listas contendo os dados das outras colunas para cada linha do arquivo CSV.
    """
    dic = {}
    with open("E:/10 - PYTHON/funcoes_python/funcoes_semana5/produtos.csv", "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)  # Pula a primeira linha do arquivo CSV
        for lista_da_linha in leitor: # Para cada linha do arquivo CSV, cria uma chave e um valor para o dicionário
            chave = lista_da_linha[indice_chave]
            valor = [item for i, item in enumerate(lista_da_linha) if i != indice_chave]
            dic[chave] = valor
    return dic

def ler_pedido(nome_arquivo):
    """Lê um arquivo CSV de pedidos e retorna uma lista de pedidos.
    Parâmetros:
        nome_arquivo: o nome do arquivo CSV a ser lido
    Retorna:
        Uma lista onde cada tupla contém o número do produto e a quantidade solicitada.
    """
    pedidos = []
    with open("E:/10 - PYTHON/funcoes_python/funcoes_semana5/pedido.csv", "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)  # Pula a primeira linha do arquivo CSV
        for lista_da_linha in leitor:
            numero_produto = lista_da_linha[0]
            quantidade = int(lista_da_linha[1])
            pedidos.append((numero_produto, quantidade))
    return pedidos

def main():

    try:
        dic_produtos = ler_dicionario("E:/10 - PYTHON/funcoes_semana5/produtos.csv", 0)
        #for chave, valor in dic_produtos.items():
            #print(f"Chave: {chave}, Valor: {valor}")
        #print("\n")

        pedidos = ler_pedido("E:/10 - PYTHON/funcoes_semana5/pedido.csv")
        quantidade_total = 0
        subtotal = 0.0
        imposto_sobre_vendas = 0.06
        imposto = 0.0
        total = 0.0
        data_e_hora_atuais = datetime.now()

        print("Recibo do pedido:\n")
        print("Vendinha do José\n")

        for numero_produto, quantidade in pedidos:
            quantidade_total += int(quantidade)
            if numero_produto in dic_produtos: #com essa trativa, evitamos o erro de KeyError caso o número do produto no pedido.csv não exista no dic_produtos
                nome_produto = dic_produtos[numero_produto][0]
                preco = float(dic_produtos[numero_produto][1])
                subtotal += preco * int(quantidade) 
                print(f"Produto: {nome_produto}, Quantidade: {quantidade}, Preço: {preco}")

        print(f"Quantidade total de produtos: {quantidade_total}")
        print(f"Subtotal: {subtotal:.2f}")
        imposto = subtotal * imposto_sobre_vendas
        print(f"Imposto sobre vendas: {imposto:.2f}")
        total = subtotal + imposto
        print(f"Total: {total:.2f}")

        print("\nObrigado pela preferência! Volte sempre!")
        print(f"Data e hora do pedido: {data_e_hora_atuais.strftime('%d/%m/%Y - %H:%M:%S')}")
        print("\n")
        print(f"Recibo gerado por: {path.basename(__file__)}")
        print(f"Você tem 30 dias para devolver os produtos, contados a partir da data do pedido.")
        print(f"A data limite para devolução é: {(data_e_hora_atuais + timedelta(days=30)).strftime('%d/%m/%Y')}")
        print("\n")

    except FileNotFoundError as e: 
        print(f"Erro: O arquivo '{e.filename}' não foi encontrado. Verifique o caminho e tente novamente.")
    except KeyError as e:
        print(f"ID de produto desconhecido no arquivo pedido.csv: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()