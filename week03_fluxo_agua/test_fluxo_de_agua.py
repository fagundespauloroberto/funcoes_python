from pytest import approx
import pytest 

from fluxo_de_agua import calc_altura_coluna_agua, calc_perda_pressao_conexoes, calc_perda_pressao_tubo
from fluxo_de_agua import calc_pressao_pela_altura, calc_num_reynolds, calc_perda_pressao_reducao_tubo, calc_metro_coluna_agua

###################
# tarefa adicional, implementado o teste para a conversão de Kilopascais para Metros de Coluna de água(MCA)
###############

def test_calcular_altura_coluna_agua():
    # Teste 1: Valores de entrada típicos
    altura_torre = 0.0
    altura_tanque = 0.0
    altura_esperada = 0.00  # Valor esperado para a altura da coluna de água (em metros)
    altura_calculada = calc_altura_coluna_agua(altura_torre, altura_tanque)
    assert altura_calculada == approx(altura_esperada, rel=1e-2)

    altura_torre = 0.0
    altura_tanque = 10.0
    altura_esperada = 7.5  # Valor esperado para a altura da coluna de água (em metros)
    altura_calculada = calc_altura_coluna_agua(altura_torre, altura_tanque)
    assert altura_calculada == approx(altura_esperada, rel=1e-2)

    altura_torre = 25.0
    altura_tanque = 0.0
    altura_esperada = 25.0  # Valor esperado para a altura da coluna de água (em metros)
    altura_calculada = calc_altura_coluna_agua(altura_torre, altura_tanque)
    assert altura_calculada == approx(altura_esperada, rel=1e-2)

    altura_torre = 48.3
    altura_tanque = 12.8
    altura_esperada = 57.9  # Valor esperado para a altura da coluna de água (em metros)
    altura_calculada = calc_altura_coluna_agua(altura_torre, altura_tanque)
    assert altura_calculada == approx(altura_esperada, rel=1e-2)    

########################################################################################
def test_calc_pressao_pela_altura():
    altura = 0.0
    pressao_esperada = 0.000  # Valor esperado para a pressão (em kPa)
    pressao_calculada = calc_pressao_pela_altura(altura)
    assert pressao_calculada == approx(pressao_esperada, rel=0.001)

    altura = 30.2
    pressao_esperada = 295.628  # Valor esperado para a pressão (em kPa)
    pressao_calculada = calc_pressao_pela_altura(altura)
    assert pressao_calculada == approx(pressao_esperada, rel=0.001)

    altura = 50.0
    pressao_esperada = 489.450  # Valor esperado para a pressão (em kPa)
    pressao_calculada = calc_pressao_pela_altura(altura)    
    assert pressao_calculada == approx(pressao_esperada, rel=0.001)

##########################################################################################
def test_calc_perda_pressao_tubo():
    diametro_tubo = 0.048692				
    comprimento_tubo = 0.00
    fator_atrito = 0.018
    velocidade_fluido = 1.75
    perda_esperada = 0.00  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)
    assert perda_calculada == approx(perda_esperada, rel=0.001)

    diametro_tubo = 0.048692	
    comprimento_tubo = 200.00	
    fator_atrito = 0.000	
    velocidade_fluido = 1.75
    perda_esperada = 0.00  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)
    assert perda_calculada == approx(perda_esperada, rel=0.001)

    diametro_tubo = 0.048692	
    comprimento_tubo = 200.00	
    fator_atrito = 0.018	
    velocidade_fluido = 0.00
    perda_esperada = 0.00  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)
    assert perda_calculada == approx(perda_esperada, rel=0.001)

    diametro_tubo = 0.048692	
    comprimento_tubo = 200.00	
    fator_atrito = 0.018	
    velocidade_fluido = 1.75
    perda_esperada = -113.008  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)
    assert perda_calculada == approx(perda_esperada, rel=0.001)

    diametro_tubo = 0.286870	
    comprimento_tubo = 1000.00	
    fator_atrito = 0.013	
    velocidade_fluido = 1.65
    perda_esperada = -61.576  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)
    assert perda_calculada == approx(perda_esperada, rel=0.001)

#####################################################################################
def test_calc_perda_pressao_conexoes():
    velocidade_fluido = 0.00
    quantidade_conexoes = 3
    perda_esperada = 0.000  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)
    assert perda_calculada == approx(perda_esperada, abs=0.001)

    velocidade_fluido = 1.65
    quantidade_conexoes = 0
    perda_esperada = 0.000  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)
    assert perda_calculada == approx(perda_esperada, abs=0.001)

    velocidade_fluido = 1.65
    quantidade_conexoes = 2
    perda_esperada = -0.109  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)
    assert perda_calculada == approx(perda_esperada, abs=0.001)

    velocidade_fluido = 1.75
    quantidade_conexoes = 2
    perda_esperada = -0.122  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)
    assert perda_calculada == approx(perda_esperada, abs=0.001)

    velocidade_fluido = 1.75
    quantidade_conexoes = 5
    perda_esperada = -0.306  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)
    assert perda_calculada == approx(perda_esperada, abs=0.001)

############################################################################
def test_calc_num_reynolds():
    diametro_hidraulico = 0.048692
    velocidade_fluido = 0.00
    reynolds_esperado = 0  # Valor esperado para o número de Reynolds
    reynolds_calculado = calc_num_reynolds(diametro_hidraulico, velocidade_fluido)
    assert reynolds_calculado == approx(reynolds_esperado, abs=1)

    diametro_hidraulico = 0.048692
    velocidade_fluido = 1.65
    reynolds_esperado = 80069  # Valor esperado para o número de Reynolds
    reynolds_calculado = calc_num_reynolds(diametro_hidraulico, velocidade_fluido)
    assert reynolds_calculado == approx(reynolds_esperado, abs=1)

    diametro_hidraulico = 0.048692
    velocidade_fluido = 1.75
    reynolds_esperado = 84922  # Valor esperado para o número de Reynolds
    reynolds_calculado = calc_num_reynolds(diametro_hidraulico, velocidade_fluido)
    assert reynolds_calculado == approx(reynolds_esperado, abs=1)

    diametro_hidraulico = 0.286870
    velocidade_fluido = 1.65
    reynolds_esperado = 471729  # Valor esperado para o número de Reynolds
    reynolds_calculado = calc_num_reynolds(diametro_hidraulico, velocidade_fluido)
    assert reynolds_calculado == approx(reynolds_esperado, abs=1)

    diametro_hidraulico = 0.286870
    velocidade_fluido = 1.75
    reynolds_esperado = 500318  # Valor esperado para o número de Reynolds
    reynolds_calculado = calc_num_reynolds(diametro_hidraulico, velocidade_fluido)
    assert reynolds_calculado == approx(reynolds_esperado, abs=1)    

##################################################################################
def test_calc_pressao_reducao_tubo():
    diametro_maior = 0.28687
    velocidade_fluido = 0.00
    numero_reynolds = 1
    diametro_menor = 0.048692
    perda_esperada = 0.000  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_fluido, numero_reynolds, diametro_menor)
    assert perda_calculada == approx(perda_esperada, abs=1)

    diametro_maior = 0.28687	
    velocidade_fluido = 1.65
    numero_reynolds = 471729
    diametro_menor = 0.048692
    perda_esperada = -163.744  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_fluido, numero_reynolds, diametro_menor)
    assert perda_calculada == approx(perda_esperada, abs=1)

    diametro_maior = 0.28687	
    velocidade_fluido = 1.75
    numero_reynolds = 500318
    diametro_menor = 0.048692
    perda_esperada = -184.182  # Valor esperado para a perda de pressão (em kPa)
    perda_calculada = calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_fluido, numero_reynolds, diametro_menor)
    assert perda_calculada == approx(perda_esperada, abs=1)

##################################################################################
def test_calc_metro_coluna_agua():
    kilopascais = 0.0
    metro_esperado = 0.0
    metro_calculado = calc_metro_coluna_agua(kilopascais)
    assert metro_calculado == approx(metro_esperado, abs=0.001)
    
    kilopascais = 100.0
    metro_esperado = 10.197
    metro_calculado = calc_metro_coluna_agua(kilopascais)
    assert metro_calculado == approx(metro_esperado, abs=0.001)

# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])