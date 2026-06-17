'''
1. Qual é o título do seu programa?
Avisa Clima(clima do tempo)

2. Que problema do mundo real o seu programa vai abordar ou ajudar a resolver?
Criar uma ferramenta leve e de facil uso com interface grafica para previsão do clima.
Sem propagandas e de facil acesso e entendimento.
Vamos buscar informações do CPTEC.
Dados meteorológicos e oceanográficos do Centro de Previsão de Tempo e
Estudos Climáticos (CPTEC/INPE).
Inclui previsões do tempo, condições atuais, informações sobre cidades e
previsões climaticas para o aeroporto.

3. O que você aprenderá ao desenvolver este programa?
Comunicação via API, recuperar dados do servidor (requests).

4. Quais módulos Python o seu programa usará?
(Alguns exemplos são: csv, datetime, functools, matplotlib, math, pandas, pytest, random, requests e tkinter.)
Vamos usar para recuperar dados o requests, fastapi, para testes o pytest e para a interface grafica, vamos usar tkinter ou kivy.
Ainda a definir conforme o entendimento durante os estudos.

5. Liste os nomes das funções de que você precisará.
(Lembre-se de que as funções mais reutilizáveis não obtêm entrada do usuário
nem imprimem resultados; em vez disso, recebem parâmetros e retornam um resultado.
Funções que obtêm entrada do usuário e imprimem resultados são
importantes e fazem um trabalho útil, mas não são facilmente reutilizáveis.)
(Lembre-se também de que é difícil testar funções que obtêm entrada do
usuário e imprimem resultados. É fácil testar funções que não obtêm entrada do
usuário nem imprimem resultados, mas que recebem parâmetros e retornam um resultado.
Portanto, você deve escrever a maior parte das funções do seu programa
para receber parâmetros e retornar um resultado.)

listar_localidades
buscar_localidades
condicoes_atuais_capitais
condicoes_atuais_aeroporto
prev_meteorolog_cidade
prev_meteorolog_6_dias
prev_meteorolog_lat_long

6. Liste os nomes das funções de teste que você escreverá.
test_buscar_localidades
test_prev_meteorolog_cidade
test_prev_meteorolog_6_dias
test_prev_meteorolog_lat_long
'''

from pytest import approx
import pytest
from avisa_clima import buscar_localidades, condicoes_atuais_capitais, prev_meteorolog_6_dias, condicoes_atuais_aeroporto
from avisa_clima import prev_meteorolog_lat_long, condicoes_atuais_capitais
import requests

def test_buscar_localidades():
    # Testa se a busca por Baje retorna uma lista e se encontra o ID correto (999)
    resultado = buscar_localidades("Bage")
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    assert resultado[0]['id'] == 694

def test_prev_meteorolog_6_dias():
    # Testa se o ID de Bage (694) retorna a estrutura correta de clima
    resultado = prev_meteorolog_6_dias(694)
    assert isinstance(resultado, dict)
    assert 'clima' in resultado
    assert len(resultado['clima']) > 0

def test_condicoes_atuais_aeroporto():
    # Testa o aeroporto de Guarulhos (SBGR)
    resultado = condicoes_atuais_aeroporto("SBGR")
    assert isinstance(resultado, dict)
    assert resultado['codigo_icao'] == "SBGR"

def test_prev_meteorolog_lat_long():
    # Testando coordenadas aproximadas de Chapeco (-27.10, -52.62)
    resultado = prev_meteorolog_lat_long(-27.10, -52.62)
    assert isinstance(resultado, dict)
    assert 'daily' in resultado
    assert 'time' in resultado['daily']

    from avisa_clima import condicoes_atuais_capitais

def test_condicoes_atuais_capitais():
    resultado = condicoes_atuais_capitais()
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    # Verifica se a primeira capital da lista tem as chaves básicas estruturadas
    assert 'nome' in resultado[0]
    assert 'estado' in resultado[0]

pytest.main(["-v", "--tb=line", "-rN", __file__])