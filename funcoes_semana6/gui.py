'''
Programa
Crie um programa Python chamado gui.py que obtenha a entrada do usuário a partir de uma GUI, execute um cálculo simples e exiba o resultado em uma GUI.
Requisitos
Seu programa deve incluir uma GUI que seja aberta quando você o executa.
A GUI deve permitir que o usuário digite informações.
Quando o usuário insere uma entrada válida, seu programa deve calcular resultados corretos e exibi-los na GUI.
Desafios Adicionais
Abaixo está uma lista de desafios adicionais que você pode fazer. Seu instrutor lhe guiará por pelo menos um deles. Fique à vontade para realizar os demais.
Adicione um botão Limpar à sua GUI, para limpar todas as entradas e saídas quando o usuário clica nele.
Adicione um rótulo que atue como uma barra de status na parte inferior da sua GUI. Seu programa deve exibir uma mensagem de erro na barra de status quando o usuário inserir uma entrada inválida. Seu programa deve limpar a barra de status quando o usuário inserir uma entrada válida.
'''

import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import Entry, _NumberEntry, IntEntry, FloatEntry
import random

def main():
    
    raiz = tk.Tk()
    janela_principal = Frame(raiz)
    janela_principal.master.title("Calculadora Simples")
    janela_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=1)
    configurar_janela(janela_principal)
    janela_principal.mainloop()

def configurar_janela(janela):
    rotulo_lados = Label(janela, text="Digite um número de lados dos seus dados (2-20):")   
    rotulo_lados.grid(row=0, column=0)
    entrada_lados = IntEntry(janela, lower_bound=2, upper_bound=20, width=5)
    entrada_lados.grid(row=0, column=1)

    rotulo_dados = Label(janela, text="Digite o número de dados a serem lançados (1-10):")
    rotulo_dados.grid(row=1, column=0)
    entrada_dados = IntEntry(janela, lower_bound=1, upper_bound=10, width=5)
    entrada_dados.grid(row=1, column=1)

    botao_lancamento = Button(janela, text="Lançar Dados")
    botao_lancamento.grid(row=2, column=0, columnspan=2, pady=10)

    rotulo_resultado = Label(janela, text="")
    rotulo_resultado.grid(row=3, column=0, columnspan=2)

    def lancar_dados(num_lados, num_dados):
        try:
            soma = 0
            resultado = ""
            for lance in range(num_dados):
                aleatorio = random.randint(1, num_lados)
                soma += aleatorio
                resultado += f"Dado {lance + 1}: {aleatorio}\n"
            lados = entrada_lados.get()
            dados = entrada_dados.get()
            resultado = [random.randint(1, lados) for _ in range(dados)]
            rotulo_resultado.config(text=f"Resultado: {resultado}")
            rotulo_resultado.config(text=f"Resultado: {resultado}\nSoma: {soma}")
            return resultado
        except ValueError:
            rotulo_resultado.config(text="Entrada inválida. Por favor, insira números válidos.")
    
    def acao_botao():
        num_lados = entrada_lados.get()
        num_dados = entrada_dados.get()
        lancar_dados(num_lados, num_dados)
        rotulo_resultado.config(text=f"Resultado: {resultado}\nSoma: {soma}")
    
    botao_lancamento.config(command=acao_botao)
    
    
if __name__ == "__main__":
    main()

