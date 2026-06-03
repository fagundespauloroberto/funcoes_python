# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

def criar_nome_completo(primeiro_nome, sobrenome):
    """Retorna uma string no formato "sobrenome; primeiro_nome". Por exemplo,
    se esta função for chamada assim:
    criar_nome_completo("Eliane", "Oliveira"), ela retornará "Oliveira; Eliane".

    Parâmetros:
        primeiro_nome: uma string que contém o primeiro nome de uma pessoa
        sobrenome: uma string que contém o sobrenome de uma pessoa
    Retorno: uma string no formato "sobrenome; primeiro_nome"
    """
    nome_completo = f"{sobrenome};{primeiro_nome}"
    return nome_completo


def extrair_sobrenome(nome_completo):
    """Extrai e retorna o sobrenome de uma string no formato:
    "sobrenome; primeiro_nome". Por exemplo, se esta função for chamada assim:
    extrair_sobrenome("Oliveira; Eliane"), ela retornará "Oliveira".

    Parâmetro:
        nome_completo: uma string no formato "sobrenome; primeiro_nome"
    Retorno: uma string contendo o sobrenome da pessoa
    """
    # Encontra o índice onde aparece "; " dentro da string do nome completo.
    indice_ponto_e_virgula = nome_completo.index("; ")

    # Extrai uma substring do nome completo e a retorna.
    sobrenome = nome_completo[0 : indice_ponto_e_virgula]
    return sobrenome


def extrair_primeiro_nome(nome_completo):
    """Extrai e retorna o primeiro nome de uma string no formato:
    "sobrenome; primeiro_nome". Por exemplo, se esta função for chamada assim:
    extrair_primeiro_nome("Oliveira; Eliane"), ela retornará "Eliane".

    Parâmetro:
        nome_completo: uma string no formato "sobrenome; primeiro_nome"
    Retorno: uma string contendo o primeiro nome da pessoa
    """
    # Encontra o índice onde aparece "; " dentro da string do nome completo.
    indice_ponto_e_virgula = nome_completo.index("/ ")

    # Extrai uma substring do nome completo e a retorna.
    primeiro_nome = nome_completo[indice_ponto_e_virgula + 2 : ]
    return primeiro_nome
