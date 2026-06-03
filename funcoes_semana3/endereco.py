# Direitos Autorais 2020, Universidade Brigham Young-Idaho. Todos os direitos reservados.

def extrair_cidade(endereco_completo):
    """Extrai e retorna o nome da cidade a partir
    de um endereço brasileiro formatado corretamente.
    
    Parâmetro:
        endereco_completo: um endereço neste formato:
            rua, número, bairro, cidade - estado, CEP
    Retorno: o nome da cidade
    """
    endereco_completo = endereco_completo.strip()
    indice_ultima_virgula = endereco_completo.rindex(",")
    indice_ultimo_hifen = endereco_completo.rindex("-", 0, indice_ultima_virgula)
    indice_virgula_cidade = endereco_completo.rindex(",", 0, indice_ultimo_hifen)
    cidade = endereco_completo[indice_virgula_cidade + 1 : indice_ultimo_hifen]
    cidade = cidade.strip()
    return cidade


def extrair_estado(endereco_completo):
    """Extrai e retorna a sigla do estado a partir
    de um endereço brasileiro formatado corretamente.
    
    Parâmetro:
        endereco_completo: um endereço neste formato:
            rua, número, bairro, cidade - estado, CEP
    Retorno: a sigla do estado (2 letras)
    """
    endereco_completo = endereco_completo.strip()
    indice_ultima_virgula = endereco_completo.rindex(",")
    indice_ultimo_hifen = endereco_completo.rindex("-", 0, indice_ultima_virgula)
    estado = endereco_completo[indice_ultimo_hifen + 1 : indice_ultima_virgula]
    estado = estado.strip()
    return estado


def extrair_cep(endereco_completo):
    """Extrai e retorna o CEP a partir
    de um endereço brasileiro formatado corretamente.
    
    Parâmetro:
        endereco_completo: um endereço neste formato:
            rua, número, bairro, cidade - estado, CEP
    Retorno: o CEP
    """
    endereco_completo = endereco_completo.strip()
    indice_ultima_virgula = endereco_completo.rindex(",")
    cep = endereco_completo[indice_ultima_virgula + 1 : ].strip()
    return cep

