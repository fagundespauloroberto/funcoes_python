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
import csv

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
    with open("E:/10 - PYTHON/funcoes_semana5/produtos.csv", "rt", encoding="utf-8") as arquivo_csv:
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
        Uma lista de tuplas, onde cada tupla contém o número do produto e a quantidade solicitada.
    """
    pedidos = []
    with open("E:/10 - PYTHON/funcoes_semana5/pedido.csv", "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)  # Pula a primeira linha do arquivo CSV
        for lista_da_linha in leitor:
            numero_produto = lista_da_linha[0]
            quantidade = int(lista_da_linha[1])
            pedidos.append((numero_produto, quantidade))
    return pedidos

def main():

    dic_produtos = ler_dicionario("E:/10 - PYTHON/funcoes_semana5/produtos.csv", 0)
    #for chave, valor in dic_produtos.items():
        #print(f"Chave: {chave}, Valor: {valor}")
    #print("\n")

    pedidos = ler_pedido("E:/10 - PYTHON/funcoes_semana5/pedido.csv")
    for numero_produto, quantidade in pedidos:
        if numero_produto in dic_produtos:
            nome_produto = dic_produtos[numero_produto][0]
            preco = float(dic_produtos[numero_produto][1])
            print(f"Produto: {nome_produto}, Quantidade: {quantidade}, Preço: {preco}")
    print("\n")

if __name__ == "__main__":
    main()