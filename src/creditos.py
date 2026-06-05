from os import get_terminal_size
from typing import Text

from utils.sistema import esperar, limpar
from utils.tui.animacao import animarEscrita, animarValor
from utils.tui.render.elementos import Ascii, Centralizado, Coluna, Tabela, Texto, centralizarTopo


def criarTrem(valor: int):
    with open("recursos/ascii/logos/logo_principal.txt", "r") as arquivo:
        ascii = arquivo.read().split("\n")
    limpar()
    largura = get_terminal_size().columns
    train = 400

    maxAltura = 7
    max = largura + train
   
    atual = largura - valor
    centralizarTopo(maxAltura)
    for i in range(maxAltura):
        esquerda = 0 if atual < 0  else atual 
        if esquerda > 0:
            print(' ' * esquerda)
        
        tremP = train if valor > train else valor
        tremI = valor - largura if valor > largura   else 0;
        
        if (valor):
            
            for j in range(tremI, tremP):
                if ascii[i] and ascii[i][j]:
                    

                    print(ascii[i][j]);
                else:
                    print(" ");
                
            
        
        print("\n");


def animarTrem():
    largura = get_terminal_size().columns
    trainLargura = 100
    max = largura + trainLargura
    animarValor(0, max, 5, criarTrem);

def mostrarIntegrantes():
    limpar()
    centralizarTopo(11)
    animarEscrita(Coluna([Ascii("recursos/ascii/logos/integrantes.txt")]))
    print("\n")
    animarEscrita(Tabela(3, [Coluna([Texto("João Lucas Silva Lopes")]), Coluna([Texto("Alan Otalvaro")]), Coluna([Texto("João Pedro Evangelista de Almeida")])]))
    esperar(1)

def mostrarLogo():
    animarTrem()

