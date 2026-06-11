# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import IntEntry

def main():
    # Cria o objeto root do Tk.
    root = tk.Tk()

    # Cria a janela principal. Em tkinter,
    # uma janela também é chamada de frame.
    frm_principal = Frame(root)
    frm_principal.master.title("Frequência Cardíaca")
    frm_principal.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Chama a função que popula a janela principal,
    # adicionando rótulos, caixas de entrada e botões.
    preencher_janela_principal(frm_principal)

    # Inicia o loop do tkinter que processa eventos do usuário
    # como pressionamentos de tecla e cliques de mouse.
    root.mainloop()

def preencher_janela_principal(frm_principal):
    """Preenche a janela principal deste programa. Em outras palavras, coloca
    os rótulos, caixas de entrada de texto e botões na janela principal.

    Parâmetro:
        frm_principal: o frame (janela) principal
    Retorno: nada
    """
    # Cria um rótulo que exibe "Idade:"
    lbl_idade = Label(frm_principal, text="Idade (12 - 90):")

    # Cria uma caixa de entrada inteira onde o usuário digitará sua idade.
    ent_idade = IntEntry(frm_principal, width=4, lower_bound=12, upper_bound=90)

    # Cria um rótulo que exibe "anos"
    lbl_unidade_idade = Label(frm_principal, text="anos")

    # Cria um rótulo que exibe "Frequências:"
    lbl_frequencias = Label(frm_principal, text="Frequências:")

    # Cria rótulos que exibirão os resultados.
    lbl_lenta = Label(frm_principal, width=3)
    lbl_rapida = Label(frm_principal, width=3)
    lbl_unidade_frequencia = Label(frm_principal, text="batimentos/minuto")

    # Cria o botão Limpar.
    btn_limpar = Button(frm_principal, text="Limpar")

    # Organiza todos os elementos em uma grade.
    lbl_idade.grid(         row=0, column=0, padx=3, pady=3)
    ent_idade.grid(         row=0, column=1, padx=3, pady=3)
    lbl_unidade_idade.grid( row=0, column=2, padx=0, pady=3)

    lbl_frequencias.grid(        row=1, column=0, padx=(30,3), pady=3)
    lbl_lenta.grid(              row=1, column=1, padx=3, pady=3)
    lbl_rapida.grid(             row=1, column=2, padx=3, pady=3)
    lbl_unidade_frequencia.grid(row=1, column=3, padx=0, pady=3)

    btn_limpar.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def calcular(event):
        """Calcula e exibe as frequências cardíacas
        benéficas mínima e máxima do usuário."""
        try:
            idade = ent_idade.get()
            freq_maxima = 220 - idade
            lenta = freq_maxima * 0.65
            rapida = freq_maxima * 0.85

            lbl_lenta.config(text=f"{lenta:.0f}")
            lbl_rapida.config(text=f"{rapida:.0f}")

        except ValueError:
            lbl_lenta.config(text="")
            lbl_rapida.config(text="")

    def limpar():
        """Limpa todas as entradas e saídas."""
        btn_limpar.focus()
        ent_idade.clear()
        lbl_lenta.config(text="")
        lbl_rapida.config(text="")
        ent_idade.focus()

    ent_idade.bind("<KeyRelease>", calcular)
    btn_limpar.config(command=limpar)
    ent_idade.focus()

if __name__ == "__main__":
    main()
