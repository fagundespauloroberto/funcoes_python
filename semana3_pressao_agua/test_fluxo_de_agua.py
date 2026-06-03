from pytest import approx
import pytest 

from fluxo_de_agua import calc_altura_coluna_agua, calc_perda_pressao_tubo, calc_pressao_pela_altura

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



# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])