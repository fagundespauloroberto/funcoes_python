'''
Requisitos do Usuário
Mariana Cardoso, a química responsável, pediu que você criasse um programa com os seguintes requisitos.
Solicitar uma fórmula química ao usuário.
Solicitar a quantidade do composto em gramas ao usuário (ou seja, massa_da_amostra).
Calcular e exibir a massa molar.
Calcular e exibir o número de mols.
Mariana forneceu as seguintes informações:

Um composto ou molécula é descrito por uma lista de elementos que ele contém. 
O elemento é identificado pelo símbolo do elemento. Se houver mais de um átomo desse 
elemento, um número representando o número de átomos no composto seguirá o símbolo do elemento. 
Aqui estão alguns exemplos:
H2O (água) tem 2 átomos de hidrogênio e 1 átomo de oxigênio.
C6H12O6 (glicose) tem 6 átomos de carbono, 12 átomos de hidrogênio e 6 átomos de oxigênio.
Para calcular a massa molar de um composto, tudo o que você precisa fazer é somar a massa de todos os átomos no composto.
Para calcular o número de mols em uma amostra, use a seguinte fórmula:
numero_mols = 
massa_da_amostra
massa_molar
'''

#####################
#Como melhoria no código, foi implementado a busca por símbolo do elemento para obter informações:
# def obter_informacoes_elemento(dic_tabela_periodica, simbolo):
# ####################

from formula import interpretar_formula
from formula import *

def criar_tabela_periodica():
    dic_tabela_periodica = {
        "Ac": ["Actínio", 227],
        "Ag": ["Prata", 107.8682],
        "Al": ["Alumínio", 26.9815386],
        "Ar": ["Argônio", 39.948],
        "As": ["Arsênio", 74.9216],
        "At": ["Astato", 210],
        "Au": ["Ouro", 196.966569],
        "B": ["Boro", 10.811],
        "Ba": ["Bário", 137.327],
        "Be": ["Berílio", 9.012182],
        "Bi": ["Bismuto", 208.9804],
        "Br": ["Bromo", 79.904],
        "C": ["Carbono", 12.0107],
        "Ca": ["Cálcio", 40.078],
        "Cd": ["Cádmio", 112.411],
        "Ce": ["Cério", 140.116],
        "Cl": ["Cloro", 35.453],
        "Co": ["Cobalto", 58.933195],
        "Cr": ["Cromo", 51.9961],
        "Cs": ["Césio", 132.9054519],
        "Cu": ["Cobre", 63.546],
        "Dy": ["Disprósio", 162.5],
        "Er": ["Érbio", 167.259],
        "Eu": ["Európio", 151.964],
        "F": ["Flúor", 18.9984032],
        "Fe": ["Ferro", 55.845],
        "Fr": ["Frâncio", 223],
        "Ga": ["Gálio", 69.723],
        "Gd": ["Gadolínio", 157.25],
        "Ge": ["Germânio", 72.64],
        "H": ["Hidrogênio", 1.00794],
        "He": ["Hélio", 4.002602],
        "Hf": ["Háfnio", 178.49],
        "Hg": ["Mercúrio", 200.59],
        "Ho": ["Hólmio", 164.93032],
        "I": ["Iodo", 126.90447],
        "In": ["Índio", 114.818],
        "Ir": ["Irídio", 192.217],
        "K": ["Potássio", 39.0983],
        "Kr": ["Criptônio", 83.798],
        "La": ["Lantânio", 138.90547],
        "Li": ["Lítio", 6.941],
        "Lu": ["Lutécio", 174.9668],
        "Mg": ["Magnésio", 24.305],
        "Mn": ["Manganês", 54.938045],
        "Mo": ["Molibdênio", 95.96],
        "N": ["Nitrogênio", 14.0067],
        "Na": ["Sódio", 22.98976928],
        "Nb": ["Nióbio", 92.90638],
        "Nd": ["Neodímio", 144.242],
        "Ne": ["Neônio", 20.1797],
        "Ni": ["Níquel", 58.6934],
        "Np": ["Neptúnio", 237],
        "O": ["Oxigênio", 15.9994],
        "Os": ["Ósmio", 190.23],
        "P": ["Fósforo", 30.973762],
        "Pa": ["Protactínio", 231.03588],
        "Pb": ["Chumbo", 207.2],
        "Pd": ["Paládio", 106.42],
        "Pm": ["Promécio", 145],
        "Po": ["Polônio", 209],
        "Pr": ["Praseodímio", 140.90765],
        "Pt": ["Platina", 195.084],
        "Pu": ["Plutônio", 244],
        "Ra": ["Rádio", 226],
        "Rb": ["Rubídio", 85.4678],
        "Re": ["Rênio", 186.207],
        "Rh": ["Ródio", 102.9055],
        "Rn": ["Radônio", 222],
        "Ru": ["Rutênio", 101.07],
        "S": ["Enxofre", 32.065],
        "Sb": ["Antimônio", 121.76],
        "Sc": ["Escândio", 44.955912],
        "Se": ["Selênio", 78.96],
        "Si": ["Silício", 28.0855],
        "Sm": ["Samário", 150.36],
        "Sn": ["Estanho", 118.71],
        "Sr": ["Estrôncio", 87.62],
        "Ta": ["Tântalo", 180.94788],
        "Tb": ["Térbio", 158.92535],
        "Tc": ["Tecnécio", 98],
        "Te": ["Telúrio", 127.6],
        "Th": ["Tório", 232.03806],
        "Ti": ["Titânio", 47.867],
        "Tl": ["Tálio", 204.3833],
        "Tm": ["Túlio", 168.93421],
        "U": ["Urânio", 238.02891],
        "V": ["Vanádio", 50.9415],
        "W": ["Tungstênio", 183.84],
        "Xe": ["Xenônio", 131.293],
        "Y": ["Ítrio", 88.90585],
        "Yb": ["Itérbio", 173.054],
        "Zn": ["Zinco", 65.38],
        "Zr": ["Zircônio", 91.224],
    }
    return dic_tabela_periodica

def obter_informacoes_elemento(dic_tabela_periodica, simbolo):
    elemento = dic_tabela_periodica.get(simbolo)
    if elemento:
        return f"Elemento: {elemento[0]}, Massa Atômica: {elemento[1]} "
    else:
        return "Elemento não encontrado na tabela periódica."
    
def calcular_massa_molar(formula, dic_tabela_periodica ):
    massa_do_elemento = 0.000000
    massa_molar = 0.000000

    if isinstance(formula, str):
        elementos_lista = interpretar_formula(formula, dic_tabela_periodica)
    else:
        elementos_lista = formula

    for simbolo, quantidade in elementos_lista:
        elemento = dic_tabela_periodica.get(simbolo)
        if elemento:
            massa_molar += elemento[1] * quantidade
        else:
            return 0.00
    return massa_molar  


def main():
    amostra = 0.000000
    mols = 0.000000
    massa_molar = 0.000000

    dic_tabela_periodica = criar_tabela_periodica()
    
    simbolo = input("Digite o símbolo do elemento para obter informações: ")
    informacoes = obter_informacoes_elemento(dic_tabela_periodica, simbolo)
    print(informacoes)
    
    formula = input("Insira a fórmula química para calcular a massa molar: ")
    amostra = float(input("Insera a massa em gramas da amostra para calcular: "))
    massa_molar = calcular_massa_molar(formula, dic_tabela_periodica)
    print(f"Massa molar de {formula}: {massa_molar:.5f} gramas/mol.")
    mols = amostra / massa_molar 
    print(f"O numero de mols na amostra: {mols:.5f} mols.")

if __name__ == "__main__":
    main()

