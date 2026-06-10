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

import random
from typing import Callable, TypeAlias

from src.banco_dados import Estado, Rodada, banco_dados
from utils.menu import menu, Opcao
from utils.tui.render.elementos import Ascii, Coluna, Tabela, Texto

# recursos/ascii/opcoes/temperatura.txt
# recursos/ascii/opcoes/comunicacao.txt
#

funcao_passiva: TypeAlias = Callable[[Rodada], None]


# dados_missao = [[temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo, temperatura_motor]]
def atribuir_vantagem(rodada: Rodada, index: int):
    rodada.parametros[index].definir_tendencia(Estado.ESTAVEL)
    rodada.parametros[index].tendencia_atual.duracao = 2


def atribuir_consequencia(rodada: Rodada, index: int):
    if rodada.parametros[index].tendencia_atual.estado == Estado.ESTAVEL:
        rodada.parametros[index].definir_tendencia(Estado.ATENCAO)
        rodada.parametros[index].tendencia_atual.duracao = 2
    elif rodada.parametros[index].tendencia_atual.estado == Estado.CRITICO:
        rodada.parametros[index].tendencia_atual.duracao += 2
    elif random.randint(0, 10) > 7:
        rodada.parametros[index].definir_tendencia(Estado.CRITICO)
        rodada.parametros[index].tendencia_atual.duracao += 2
    else:
        rodada.parametros[index].tendencia_atual.duracao += 2

def ligar_refrigerador(rodada: Rodada):
    # rodada.parametros[]
    atribuir_vantagem(rodada, 0)
    # dados[0] -= 10
    atribuir_consequencia(rodada, 3)


def verificar_frequencia(rodada: Rodada):
    atribuir_vantagem(rodada, 1)
    # /dados[1] +=15


def ligar_gerador(rodada: Rodada):
    rodada.tempo_final += 2
    atribuir_vantagem(rodada, 2)
    # dados[2] += 15
    # tempo -= 10


def gerar_oxigenio(rodada: Rodada):
    atribuir_vantagem(rodada, 3)
    atribuir_consequencia(rodada, 2)
    


def estabilizar(rodada: Rodada):
    atribuir_vantagem(rodada, 4)
    atribuir_consequencia(rodada, 3)
    # dados[2] -= 10


def reparar_nave(rodada: Rodada):
    atribuir_vantagem(rodada, 5)
    atribuir_consequencia(rodada, 0)
    atribuir_consequencia(rodada, 3)
   


# def modo_economia(rodada: Rodada):
#     atribuir_vantagem(rodada, 2)
#     rodada.tempo_final += 6


# def aumentar_velocidade(dados : Dados_Atuais):
#     global tempo
#     dados[2] -= 10
#     rodada.
#     tempo -= 10

# def ligar_aquecedor(dados : Dados_Atuais):
#     dados[0] += 10
#     dados[2] -= 10


def passivo(funcao: funcao_passiva):
    def a():
        funcao(banco_dados.rodada)

    return a


def menuAcoes():
    menu(
        "Ações",
        [
            Opcao(
                Coluna(
                    [
                        Texto("1. ligar controlador de temperatura"),
                        Texto("positivo: temperatura, negativo: energia"),
                        Ascii("recursos/ascii/opcoes/temperatura.txt"),
                    ]
                ),
                passivo(ligar_refrigerador),
            ),
            Opcao(
                Coluna(
                    [
                        Texto("2. verificar frequencia de radio"),
                        Texto("positivo: comunicação"),
                        Ascii(
                            "recursos/ascii/opcoes/comunicacao.txt",
                        ),
                    ]
                ),
                passivo(verificar_frequencia),
            ),
            Opcao(
                Coluna(
                    [
                        Texto("3. ligar geraradores"),
                        Texto("positivo: energia, negativo: tempo(+2 ciclos)"),
                        Ascii("recursos/ascii/opcoes/bateria.txt"),
                    ]
                ),
                passivo(ligar_gerador),
            ),
            Opcao(
                Coluna(
                    [
                        Texto("4. ativar gerador oxigenio"),
                        Texto("positivo: oxigenio, negativo: energia"),
                        Ascii("recursos/ascii/opcoes/oxigenio.txt"),
                    ]
                ),
                passivo(gerar_oxigenio),
            ),
            # Opcao(Coluna([Texto("reduzir operações não essenciais"), Ascii("recursos/ascii/opcoes/estabilidade.txt")]),passivo(estabilizar)),
            Opcao(
                Coluna(
                    [
                        Texto("5. reparar nave"),
                        Texto("positivo: integridade, negativo: temperatura, oxigenio"),
                        Ascii("recursos/ascii/opcoes/integridade.txt"),
                    ]
                ),
                passivo(reparar_nave),
            ),
            # Opcao(Coluna([Texto("6. ligar refrigerador do motor"), Ascii("recursos/ascii/opcoes/temperatura_motor.txt")]),passivo(temperatura_motor)),
            Opcao(
                Coluna(
                    [
                        Texto("6. estabilizar"),
                        Texto("positivo: estabilidade, negativo: comunicacao"),
                        Ascii("recursos/ascii/opcoes/velocidade.txt"),
                    ]
                ),
                passivo(estabilizar),
            ),
            # Opcao(Coluna([Texto("7. ligar aquecedor"), Ascii("recursos/ascii/opcoes/aquecedor.txt")]),passivo(ligar_aquecedor)),
            # Opcao(Coluna([Texto("8. aumentar velocidade"), Ascii("recursos/ascii/opcoes/velocidade.txt")]),passivo(aumentar_velocidade))
        ],
    )
    # print(Tabela(3, [
    #     Coluna([Texto("ligar resfrigerador"), Ascii("recursos/ascii/opcoes/temperatura.txt")]),
    #     Coluna([Texto("verificar frequencia de radio"), Ascii("recursos/ascii/opcoes/comunicacao.txt")]),
    #     Coluna([Texto("usar combustivel de reserva/ligar geraradores"), Ascii("recursos/ascii/opcoes/bateria.txt")]),
    #     Coluna([Texto("ativar gerador oxigenio"), Ascii("recursos/ascii/opcoes/oxigenio.txt")]),
    #     #Coluna([Texto("reduzir operações não essenciais"), Ascii("recursos/ascii/opcoes/estabilidade.txt")]),
    #     Coluna([Texto("reparar nave"), Ascii("recursos/ascii/opcoes/integridade.txt")]),
    #     Coluna([Texto("ligar refrigerador do motor"), Ascii("recursos/ascii/opcoes/temperatura_motor.txt")]),
    #     Coluna([Texto("ativar modo economia"), Ascii("recursos/ascii/opcoes/economia.txt")]),
    #     Coluna([Texto("ligar aquecedor"), Ascii("recursos/ascii/opcoes/aquecedor.txt")]),
    #     Coluna([Texto("aumentar velocidade"), Ascii("recursos/ascii/opcoes/velocidade.txt")])
    # ]).renderizar())
