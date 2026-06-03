from nomes import criar_nome_completo

import pytest

def test_criar_nome_completo():
    primeiro_nome = "Eliane"
    
    segundo_nome = "Oliveira"
    
    #resultado = "Oliveira; Eliane"
    #saida = criar_nome_completo(primeiro_nome, segundo_nome)
    #assert saida == resultado

    resultado = criar_nome_completo(primeiro_nome, segundo_nome)
    assert resultado == "Oliveira; Eliane"
    #assert resultado == "Eliane Oliveira"
    
pytest.main(["-v", "--tb=line", "-rN", __file__])