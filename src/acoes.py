# verificar frequencia de radio (+comunicacao) 
# ligar aquecedor
# ligar resfrigerador (-energia -temperatura)
# ligar aquecedor (-energia + temperatura)
# reparar nave (+integridade -oxigenio -temperatura)
# ativar gerador oxigenio (+oxigenio, -energia)
# aumentar velocidade (+tempo de navegacao, -energia)
# usar combustivel de reserva/ligar geraradores(+energia, -tempo)
# ativar modo economia (~energia, -tempo)
# estabilizar recursos do sistema (+estabilidade, -energia)

from typing import Callable, TypeAlias

from utils.menu import menu, Opcao
from utils.tui.render.elementos import Ascii, Coluna, Tabela, Texto
from src.dados import Dados_Atuais, dados_atuais
# recursos/ascii/opcoes/temperatura.txt
# recursos/ascii/opcoes/comunicacao.txt
# 

funcao_passiva: TypeAlias = Callable[[Dados_Atuais], None]

tempo = 10

#dados_missao = [[temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo, temperatura_motor]]
def ligar_refrigerador(dados: Dados_Atuais):
    dados[0] -= 10
    dados[3] -= 5
    
    
def verificar_frequencia(dados : Dados_Atuais):
    dados[1] +=15

def ligar_gerador(dados : Dados_Atuais):
    global tempo
    dados[2] += 15
    tempo -= 10

def gerar_oxigenio(dados : Dados_Atuais):
    dados[3] += 15
    dados[2] -= 10

def estabilizar(dados : Dados_Atuais):
    dados[4] += 15
    dados[2] -= 10

def reparar_nave(dados : Dados_Atuais):
    dados[5] += 15
    dados[3] -= 10
    dados[0] -= 10

def temperatura_motor(dados : Dados_Atuais):
    dados[6] += 15   
    dados[0] -= 10
    dados[2] -= 10

def modo_economia(dados : Dados_Atuais):
    global tempo
    dados[2] 
    tempo -= 10
    
def aumentar_velocidade(dados : Dados_Atuais):
    global tempo
    dados[2] -= 10
    tempo -= 10

def ligar_aquecedor(dados : Dados_Atuais):
    dados[0] += 10
    dados[2] -= 10
    
def passivo(funcao: funcao_passiva):
    def a():
        funcao(dados_atuais)
    return a

def menuAcoes():
    menu("Ações", [
        Opcao(Coluna([Texto("ligar resfrigerador"), Ascii("recursos/ascii/opcoes/temperatura.txt")]), passivo(ligar_refrigerador)),
        Opcao(Coluna([Texto("verificar frequencia de radio"), Ascii("recursos/ascii/opcoes/comunicacao.txt", )]),passivo(verificar_frequencia)),
        Opcao(Coluna([Texto("usar combustivel de reserva/ligar geraradores"), Ascii("recursos/ascii/opcoes/bateria.txt")]),passivo(ligar_gerador)),
        Opcao(Coluna([Texto("ativar gerador oxigenio"), Ascii("recursos/ascii/opcoes/oxigenio.txt")]),passivo(gerar_oxigenio)),
        #Opcao(Coluna([Texto("reduzir operações não essenciais"), Ascii("recursos/ascii/opcoes/estabilidade.txt")]),passivo(estabilizar)),
        Opcao(Coluna([Texto("reparar nave"), Ascii("recursos/ascii/opcoes/integridade.txt")]), passivo(reparar_nave)),
        Opcao(Coluna([Texto("ligar refrigerador do motor"), Ascii("recursos/ascii/opcoes/temperatura_motor.txt")]),passivo(temperatura_motor)),
        Opcao(Coluna([Texto("ativar modo economia"), Ascii("recursos/ascii/opcoes/economia.txt")]),passivo(modo_economia)),
        Opcao(Coluna([Texto("ligar aquecedor"), Ascii("recursos/ascii/opcoes/aquecedor.txt")]),passivo(ligar_aquecedor)),
        Opcao(Coluna([Texto("aumentar velocidade"), Ascii("recursos/ascii/opcoes/velocidade.txt")]),passivo(aumentar_velocidade))
    ])
    print(Tabela(3, [
        Coluna([Texto("ligar resfrigerador"), Ascii("recursos/ascii/opcoes/temperatura.txt")]),
        Coluna([Texto("verificar frequencia de radio"), Ascii("recursos/ascii/opcoes/comunicacao.txt")]),
        Coluna([Texto("usar combustivel de reserva/ligar geraradores"), Ascii("recursos/ascii/opcoes/bateria.txt")]),
        Coluna([Texto("ativar gerador oxigenio"), Ascii("recursos/ascii/opcoes/oxigenio.txt")]),
        #Coluna([Texto("reduzir operações não essenciais"), Ascii("recursos/ascii/opcoes/estabilidade.txt")]),
        Coluna([Texto("reparar nave"), Ascii("recursos/ascii/opcoes/integridade.txt")]),
        Coluna([Texto("ligar refrigerador do motor"), Ascii("recursos/ascii/opcoes/temperatura_motor.txt")]),
        Coluna([Texto("ativar modo economia"), Ascii("recursos/ascii/opcoes/economia.txt")]),
        Coluna([Texto("ligar aquecedor"), Ascii("recursos/ascii/opcoes/aquecedor.txt")]),
        Coluna([Texto("aumentar velocidade"), Ascii("recursos/ascii/opcoes/velocidade.txt")])
    ]).renderizar())


