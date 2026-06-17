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

import requests
import tkinter as tk
from tkinter import Frame, Label, Button, Text, Radiobutton, StringVar
from datetime import datetime
from PIL import Image, ImageTk  # Módulo necessário para as imagens de fundo

# URL base do BrasilAPI para os dados do CPTEC
BASE_URL = "https://brasilapi.com.br/api/cptec/v1"
# URL base do Open-Meteo para Lat/Long
BASE_URL_METEO = "https://api.open-meteo.com/v1/forecast"

# Dicionário global para compartilhar os componentes da interface entre as funções
componentes = {}

# Dicionário para traduzir os dias da semana retornados pela API (0-6) para nomes legíveis
DIAS_SEMANA = {
    0: "Segunda-feira",
    1: "Terça-feira",
    2: "Quarta-feira",
    3: "Quinta-feira",
    4: "Sexta-feira",
    5: "Sábado",
    6: "Domingo"
}

# --- FUNÇÕES DE LÓGICA DE NEGÓCIO (API) ---
def listar_localidades():
    """Retorna todas as localidades que o CPTEC possui no banco."""
    url = f"{BASE_URL}/cidade"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def buscar_localidades(nome_cidade: str):
    """Busca o ID e dados de uma cidade específica pelo nome."""
    url = f"{BASE_URL}/cidade/{nome_cidade}"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def condicoes_atuais_capitais():
    """Retorna as condições meteorológicas atuais nas capitais brasileiras."""
    url = f"{BASE_URL}/clima/capital"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def condicoes_atuais_aeroporto(codigo_icao: str):
    """Retorna as condições atuais no aeroporto solicitado (Ex: SBGR para Guarulhos)."""
    url = f"{BASE_URL}/clima/aeroporto/{codigo_icao}"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def prev_meteorolog_cidade(cidade_id: int):
    """Retorna a previsão do tempo para uma cidade específica para 1 dia pelo ID."""
    url = f"{BASE_URL}/clima/previsao/{cidade_id}"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def prev_meteorolog_6_dias(cidade_id: int):
    """Retorna a previsão do tempo para os próximos 6 dias pelo ID da cidade."""
    # Nota: No BrasilAPI o endpoint para múltiplos dias adiciona os dias no final da URL
    url = f"{BASE_URL}/clima/previsao/{cidade_id}/6"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()


def prev_meteorolog_lat_long(lat: float, lon: float):
    """Busca a previsão para os próximos 6 dias usando a API Open-Meteo."""
    url = f"{BASE_URL_METEO}?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,uv_index_max&timezone=auto"
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.json()

# problema encontrado nos testes, correção para o formato de data e dia da semana
def formatar_data_e_semana(data_texto: str) -> str:
    """
    Recebe uma string 'YYYY-MM-DD' e retorna 'DD/MM/YYYY (Dia da Semana)'.
    Se houver falha na conversão, retorna o texto original.
    """
    try:
        # Converte a string da API para um objeto datetime
        objeto_data = datetime.strptime(data_texto, "%Y-%m-%d")
        
        # Formata para o padrão brasileiro
        data_formatada = objeto_data.strftime("%d/%m/%Y")
        
        # Pega o número do dia da semana (0 a 6) e busca a tradução
        dia_semana_num = objeto_data.weekday()
        dia_semana_texto = DIAS_SEMANA.get(dia_semana_num, "")
        
        return f"{data_formatada} ({dia_semana_texto})"
    except Exception:
        return data_texto

# FUNÇÃO PARA ATUALIZAR A IMAGEM DE FUNDO BASEADA NA CONDIÇÃO DO TEMPO

def atualizar_imagem_fundo(condicao_texto: str):
    """Muda a imagem de fundo baseada na descrição do tempo. Baixa da internet se não existir."""
    condicao_texto = condicao_texto.lower()
    
    # Mapeamento de condições para arquivos locais e URLs de download rápido
    if "chuva" in condicao_texto or "chuvoso" in condicao_texto or "pancadas" in condicao_texto:
        arquivo = "chuvoso.jpg"
        url_reserva = "https://images.unsplash.com/photo-1534274988757-a28bf1a57c17?w=650&q=80"
    elif "nublado" in condicao_texto or "encoberto" in condicao_texto or "parcialmente" in condicao_texto:
        arquivo = "nublado.jpg"
        url_reserva = "https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=650&q=80"
    else:
        arquivo = "ensolarado.jpg"
        url_reserva = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=650&q=80"

    import os
    # Se o arquivo não existir na pasta, o Python baixa ele automaticamente para você!
    if not os.path.exists(arquivo):
        try:
            print(f"Baixando imagem de amostra para '{arquivo}'...")
            img_data = requests.get(url_reserva).content
            with open(arquivo, 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Não foi possível baixar a imagem de amostra: {e}")

    try:
        imagem_original = Image.open(arquivo)
        imagem_redimensionada = imagem_original.resize((650, 520), Image.Resampling.LANCZOS)
        foto = ImageTk.PhotoImage(imagem_redimensionada)
        
        componentes['label_fundo'].config(image=foto)
        componentes['label_fundo'].image = foto
    except Exception as e:
        print(f"Erro ao carregar a imagem de fundo: {e}")

# FUNÇÕES DA INTERFACE GRÁFICA **********************************************
def alternar_modo_busca():
    """Modifica a interface dependendo do modo de busca selecionado."""
    modo = componentes['modo_busca'].get()
    
    if modo == "cidade":
        componentes['rotulo_dinamico'].config(text="Digite o nome da cidade:")
        componentes['entrada_cidade'].grid()
        componentes['moldura_lat_lon'].grid_remove()
        # Mostra as opções de dias apenas para o modo cidade
        componentes['moldura_periodo'].grid()
    elif modo == "lat_lon":
        componentes['rotulo_dinamico'].config(text="Digite as coordenadas:")
        componentes['entrada_cidade'].grid_remove()
        componentes['moldura_lat_lon'].grid()
    else:  # Modo capitais
        componentes['rotulo_dinamico'].config(text="Clique no botão abaixo para listar:")
        componentes['entrada_cidade'].grid_remove()
        componentes['moldura_lat_lon'].grid_remove()


def configurar_janela(janela):
    # Rótulo invisível que servirá como nossa imagem de fundo (Backdrop)
    label_fundo = Label(janela)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    componentes['label_fundo'] = label_fundo

    # Criamos uma Moldura Transparente superior para os controles para não sumirem no fundo
    moldura_controles = Frame(janela, bg="#ffffff", bd=1, relief=tk.SOLID)
    moldura_controles.pack(padx=15, pady=10, fill=tk.X)

    componentes['modo_busca'] = StringVar(value="cidade")
    componentes['periodo_dias'] = StringVar(value="6")
    
    Radiobutton(moldura_controles, text="Por Cidade", variable=componentes['modo_busca'], value="cidade", command=alternar_modo_busca, bg="#ffffff").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    Radiobutton(moldura_controles, text="Por Lat / Long", variable=componentes['modo_busca'], value="lat_lon", command=alternar_modo_busca, bg="#ffffff").grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
    
    componentes['rotulo_dinamico'] = Label(moldura_controles, text="Digite o nome da cidade:", font=("Arial", 10, "bold"), bg="#ffffff")
    componentes['rotulo_dinamico'].grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    componentes['entrada_cidade'] = tk.Entry(moldura_controles, width=25, font=("Arial", 11))
    componentes['entrada_cidade'].grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    # Container Lat/Long
    moldura_lat_lon = Frame(moldura_controles, bg="#ffffff")
    componentes['moldura_lat_lon'] = moldura_lat_lon
    Label(moldura_lat_lon, text="Lat:", bg="#ffffff").pack(side=tk.LEFT)
    componentes['entrada_lat'] = tk.Entry(moldura_lat_lon, width=8)
    componentes['entrada_lat'].pack(side=tk.LEFT, padx=2)
    Label(moldura_lat_lon, text="Long:", bg="#ffffff").pack(side=tk.LEFT, padx=2)
    componentes['entrada_lon'] = tk.Entry(moldura_lat_lon, width=8)
    componentes['entrada_lon'].pack(side=tk.LEFT, padx=2)

    # Container Período
    moldura_periodo = Frame(moldura_controles, bg="#ffffff")
    componentes['moldura_periodo'] = moldura_periodo
    moldura_periodo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
    Label(moldura_periodo, text="Período:", font=("Arial", 9, "bold"), bg="#ffffff").pack(side=tk.LEFT, padx=(0, 5))
    Radiobutton(moldura_periodo, text="1 Dia", variable=componentes['periodo_dias'], value="1", bg="#ffffff").pack(side=tk.LEFT)
    Radiobutton(moldura_periodo, text="6 Dias", variable=componentes['periodo_dias'], value="6", bg="#ffffff").pack(side=tk.LEFT)

    botao_buscar = Button(moldura_controles, text="Buscar Previsão", command=acao_botao, font=("Arial", 10, "bold"), bg="#1e88e5", fg="white")
    botao_buscar.grid(row=3, column=0, columnspan=2, pady=5)
    
    # Caixa de texto com opacidade simulada (fundo levemente acinzentado/gelo para contraste)
    componentes['area_texto'] = Text(janela, width=65, height=14, wrap=tk.WORD, font=("Consolas", 10), bg="#f4f6f7", fg="#2c3e50")
    componentes['area_texto'].pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
    componentes['area_texto'].insert(tk.END, "Aguardando busca...")
    
    alternar_modo_busca()  # Configura a interface para o modo inicial


def acao_botao():
    ent_nome_cidade = componentes['entrada_cidade']
    area_texto = componentes['area_texto']
    modo = componentes['modo_busca'].get()
    
    nome_cidade = ent_nome_cidade.get().strip()

    #limpa a área de texto antes de mostrar novos resultados
    area_texto.delete(1.0, tk.END)

    if modo == "cidade":
        periodo = componentes['periodo_dias'].get() # Recupera a escolha de 1 ou 6 dias
        
        if not nome_cidade:
            area_texto.insert(tk.END, "Por favor, insira o nome de uma cidade.")
            return
        
        area_texto.insert(tk.END, f"Buscando previsão para '{nome_cidade}'...\n")

        try:
            cidades_encontradas = buscar_localidades(nome_cidade)
            if cidades_encontradas:
                
                # === tratativa para erro de tipo, encontramos nos testes... ===
                # Se a API retornar uma lista de cidades, pegamos a primeira [0]
                if isinstance(cidades_encontradas, list):
                    dados_cidade = cidades_encontradas[0]
                # Se a API retornar um dicionário direto, usamos ele mesmo
                elif isinstance(cidades_encontradas, dict):
                    dados_cidade = cidades_encontradas
                else:
                    area_texto.insert(tk.END, "Formato de dados inesperado recebido da API.")
                    return
                
                id_cidade = dados_cidade['id']
                nome_cidade_formatado = f"{dados_cidade['nome']}  - {dados_cidade['estado']}"

                area_texto.insert(tk.END, f"Cidade encontrada: {nome_cidade_formatado} (ID: {id_cidade})\n")
                area_texto.insert(tk.END, f"Buscando previsão de {periodo} dias para {nome_cidade_formatado}...\n")

                # Lógica condicional para definir qual função chamar baseada no Período
                if periodo == "1":
                    dados_previsao = prev_meteorolog_cidade(id_cidade)
                    texto_titulo = f"=== Previsão Atual (1 Dia): {nome_cidade_formatado} ===\n\n"
                else:
                    dados_previsao = prev_meteorolog_6_dias(id_cidade)
                    texto_titulo = f"=== Previsão Estendida (6 Dias): {nome_cidade_formatado} ===\n\n"

                #limpa a área de texto antes de mostrar a previsão
                area_texto.delete(1.0, tk.END)
                area_texto.insert(tk.END, f"Previsão para {nome_cidade_formatado}:\n")

                #percorre lista de previsões diárias e formata a saída
                lista_dias = dados_previsao.get('clima', [])

                if lista_dias:

                    # MUDANÇA VISUAL: Pega a condição do primeiro dia retornado para mudar o fundo
                    condicao_amanha = lista_dias[0].get('condicao_desc', 'Ensolarado')
                    atualizar_imagem_fundo(condicao_amanha)

                    for dia in lista_dias:
                        data = formatar_data_e_semana(dia.get('data'))
                        condicao_atual = dia.get('condicao_desc', 'Não informada')
                        temp_min = dia.get('min', '--')
                        temp_max = dia.get('max', '--')
                        uv = dia.get('indice_uv', '--')

                        texto_previsao = (f"{data}: {condicao_atual}, Min: {temp_min}°C, Max: {temp_max}°C, UV: {uv}\n")
                        area_texto.insert(tk.END, texto_previsao + "-"*40 + "\n") 
                else:
                    area_texto.insert(tk.END, "Previsão não disponível para esta cidade.")

            else:
                area_texto.delete(1.0, tk.END)
                area_texto.insert(tk.END, "Cidade não encontrada na base de dados do CPTEC.")

        except requests.exceptions.RequestException as e:
            area_texto.insert(tk.END, f"Erro de conexão com o Servidor: {e}")
        except Exception as e:
            area_texto.insert(tk.END, f"Ocorreu um erro, por favor tente novamente: {e}")
    
    elif modo == "lat_lon":  # Modo Lat / Long
        str_lat = componentes['entrada_lat'].get().strip()
        str_lon = componentes['entrada_lon'].get().strip()
        
        if not str_lat or not str_lon:
            area_texto.insert(tk.END, "Por favor, insira a Latitude e a Longitude.")
            return
        
        try:
            lat = float(str_lat)
            lon = float(str_lon)
            area_texto.insert(tk.END, f"Buscando coordenadas ({lat}, {lon}) via Open-Meteo...\n")
            
            dados_previsao = prev_meteorolog_lat_long(lat, lon)
            daily = dados_previsao.get('daily', {})
            
            area_texto.delete(1.0, tk.END)
            area_texto.insert(tk.END, f"=== Previsão por Coordenadas ({lat}, {lon}) ===\n\n")
            
            # Como a Open-Meteo não traz texto direto, estimamos o fundo pelas temperaturas ou um padrão
            atualizar_imagem_fundo("Ensolarado")
            # Open-Meteo retorna listas separadas para cada dado, mapeamos pelo índice
            datas = daily.get('time', [])
            maximas = daily.get('temperature_2m_max', [])
            minimas = daily.get('temperature_2m_min', [])
            uvs = daily.get('uv_index_max', [])
            
            for i in range(min(6, len(datas))):
                data_bonita = formatar_data_e_semana(datas[i])
                texto_previsao = f"{data_bonita}\nMín: {minimas[i]}°C | Máx: {maximas[i]}°C | UV: {uvs[i]}\n"
                area_texto.insert(tk.END, texto_previsao + "-"*60 + "\n")
                
        except ValueError:
            area_texto.insert(tk.END, "Por favor, digite apenas números válidos para Latitude e Longitude.")
        except Exception as e:
            area_texto.insert(tk.END, f"Erro ao processar dados de Coordenadas: {e}")
    
    else:  # === MODO NOVO: RESUMO DAS CAPITAIS ===
        area_texto.insert(tk.END, "Consultando condições atuais nas capitais brasileiras...\n")
        try:
            lista_capitais = condicoes_atuais_capitais()
            
            area_texto.delete(1.0, tk.END)
            area_texto.insert(tk.END, "=== Condições Atuais nas Capitais Brasileiras ===\n\n")
            
            # Formatação compacta em colunas para caber várias na mesma tela
            for cap in lista_capitais:
                nome = cap.get('nome')
                uf = cap.get('estado')
                condicao = cap.get('condicao_desc', 'Não informada')
                minima = cap.get('min', '--')
                maxima = cap.get('max', '--')
                
                texto_cap = f"{nome} ({uf}): {condicao}\n👉 Mín: {minima}°C | Máx: {maxima}°C\n"
                area_texto.insert(tk.END, texto_cap + "."*45 + "\n")
                
        # ERROS DE SERVIDOR (HTTPError) ===
        except requests.exceptions.HTTPError as e:
            area_texto.delete(1.0, tk.END)
            if e.response.status_code == 500:
                area_texto.insert(tk.END, "⚠️ O servidor do BrasilAPI/CPTEC está instável ou fora do ar no momento (Erro 500).\n\nPor favor, tente novamente em alguns minutos ou utilize a busca por Cidade/Coordenadas.")
            else:
                area_texto.insert(tk.END, f"Erro HTTP do servidor: {e.response.status_code}")
        except Exception as e:
            area_texto.insert(tk.END, f"Erro ao buscar condições das capitais: {e}")


# --- Função Principal do programa... ---
def main():
    #print("=== Bem-vindo ao Avisa Clima ===\n")
    raiz = tk.Tk()

    #ajuste para o tamanho da janela, pode ser modificado conforme necessidade
    raiz.geometry("600x420")
    raiz.minsize(600, 420)

    #janela_principal = Frame(raiz)
    #janela_principal.master.title("Avisa Clima - Previsão do Tempo")
    #janela_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
    #configurar_janela(janela_principal)
    #janela_principal.mainloop()
    configurar_janela(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()