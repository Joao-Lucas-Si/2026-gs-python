import random
from typing import TypedDict

from cycler import V

from src.acoes import menuAcoes
from src.banco_dados import banco_dados
from src.recomendacao import (
    Estado,
    estado_bateria,
    estado_comunicacao,
    estado_estabilidade,
    estado_integridade,
    estado_motor,
    estado_oxigenio,
    estado_temperatura,
)
from utils.input import estaPressionado
from utils.menu import Opcao, menu
from utils.sistema import esperar, limpar, pausar

from utils.tui.efeitos import CorAlvo, Cores1B
from utils.tui.render.elementos import (
    Alinhamento,
    Ascii,
    AsciiAnimado,
    Coluna,
    Elemento,
    Preencher,
    Tabela,
    Texto,
)
from src.dados import dados_missao, dados_atuais


class ValorDado:
    valor: int | float = 2
    estado: str = "NORMAL"
    comentario: str = "ESTAVEL"

    def __init__(self, valor: float | int, estado: str, comentario: str) -> None:
        self.valor = valor
        self.estado = estado
        self.comentario = comentario


def ciclo_tabela(
    temperatura: ValorDado,
    comunicacao: ValorDado,
    bateria: ValorDado,
    oxigenio: ValorDado,
    estabilidade: ValorDado,
    integridade_modulo: ValorDado,
    temperatura_motor: ValorDado,
) -> Elemento:
    return Tabela(
        4,
        [
            Coluna([Texto("temperatura")]),
            Coluna([Texto(f"{temperatura.valor}")]),
            Coluna([Texto(f"{temperatura.estado}")]),
            Coluna([Texto(f"{temperatura.comentario}")]),
            Coluna([Texto("Comunicacao")]),
            Coluna([Texto(f"{comunicacao.valor}")]),
            Coluna([Texto(f"{comunicacao.estado}")]),
            Coluna([Texto(f"{comunicacao.comentario}")]),
            Coluna([Texto("Energia")]),
            Coluna([Texto(f"{bateria.valor:.2f}")]),
            Coluna([Texto(f"{bateria.estado}")]),
            Coluna([Texto(f"{bateria.comentario}")]),
            Coluna([Texto("Oxigênio")]),
            Coluna([Texto(f"{oxigenio.valor}")]),
            Coluna([Texto(f"{oxigenio.estado}")]),
            Coluna([Texto(f"{oxigenio.comentario}")]),
            Coluna([Texto("Estabilidade")]),
            Coluna([Texto(f"{estabilidade.valor}")]),
            Coluna([Texto(f"{estabilidade.estado}")]),
            Coluna([Texto(f"{estabilidade.comentario}")]),
            Coluna([Texto("integridade do modulo")]),
            Coluna([Texto(f"{integridade_modulo.valor}")]),
            Coluna([Texto(f"{integridade_modulo.estado}")]),
            Coluna([Texto(f"{integridade_modulo.comentario}")]),
            Coluna([Texto("temperatura do motor")]),
            Coluna([Texto(f"{temperatura_motor.valor}")]),
            Coluna([Texto(f"{temperatura_motor.estado}")]),
            Coluna([Texto(f"{temperatura_motor.comentario}")]),
        ],
    )


# for dados in dados_missao:
#     ciclo_tabela(dados[0], dados[1])

# ciclo_tabela(10, 10)


def cabecalho(ciclos):
    print(
        Coluna(
            [
                Coluna(
                    [
                        Preencher("="),
                        Texto("MISSION CONTROL"),
                        Preencher("="),
                        Texto(
                            "Missão ficar rico"
                            + "\n"
                            + "Equipe: Equipe Alpha"
                            + "\n"
                            + f"Ciclos analisados: {ciclos}"
                        ),
                        Preencher("="),
                    ],
                    alinhamento=Alinhamento.ESQUERDA,
                ),
            ]
        ).renderizar()
    )


def ciclo(ciclos):
    def nothing():
        pass

    esperar(0.5)
    menu(
        "Relatorio ciclo",
        [
            Opcao(Coluna([Texto("continuar?")]), nothing),
            Opcao(Coluna([Texto("abrir ações")]), menuAcoes),
        ],
        colunas=2,
        top=lambda: Tabela(
            2,
            [
                Coluna(
                    [
                        Texto(f"Ciclo {ciclos}"),
                        ciclo_tabela(
                            ValorDado(
                                dados_atuais[0],
                                estado_temperatura(dados_atuais[0]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[1],
                                estado_comunicacao(dados_atuais[1]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[2],
                                estado_bateria(dados_atuais[2]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[3],
                                estado_oxigenio(dados_atuais[3]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[4],
                                estado_estabilidade(dados_atuais[4]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[5],
                                estado_integridade(dados_atuais[5]).name,
                                "",
                            ),
                            ValorDado(
                                dados_atuais[6], estado_motor(dados_atuais[6]).name, ""
                            ),
                        ),
                    ]
                ),
                Coluna([Ascii("recursos/ascii/naves/foguete_medio.txt")]),
            ],
        ),
    )


# recursos/ascii/naves/foguete_medio.txt
def gerenciar_ciclo():
    total_ciclo = 1
    cabecalho(total_ciclo)
    while banco_dados.tempo > 0:
        limpar()
        ciclo(total_ciclo)
        total_ciclo += 1
        banco_dados.tempo -= 1
        dados_atuais[2] -= random.randint(5, 15)
        dados_atuais[1] -= random.randint(1, 5)
        dados_atuais[0] += random.randint(-5, 5)
        dados_atuais[3] -= random.randint(1, 5)

       
        if estado_temperatura(dados_atuais[0]) == Estado.MORTIFERO or estado_comunicacao(dados_atuais[1]) == Estado.MORTIFERO or estado_bateria(dados_atuais[2]) == Estado.MORTIFERO or estado_oxigenio(dados_atuais[3]) == Estado.MORTIFERO or estado_estabilidade(dados_atuais[4]) == Estado.MORTIFERO or estado_integridade(dados_atuais[5]) == Estado.MORTIFERO or estado_motor(dados_atuais[6]) == Estado.MORTIFERO:
            break

    if banco_dados.tempo > 0:
        derrota()
    else:
        banco_dados.pontos += sum(
            map(lambda material: material.value.valor, banco_dados.asteroide.materiais)
        )

        vitoria()

class Dado(TypedDict):
    dado: str
    estado: Estado

def derrota():
    i = 0
    estados: list[Dado] = [
        {"estado": estado_temperatura(dados_atuais[0]), "dado": "temperatura"},
        {"estado": estado_comunicacao(dados_atuais[1]), "dado": "comunicação"},
        {"estado": estado_bateria(dados_atuais[2]),"dado": "bateria"},
        {"estado": estado_oxigenio(dados_atuais[3]),"dado": "oxigenio"},
        {"estado": estado_estabilidade(dados_atuais[4]),"dado": "estabilidade"},
        {"estado": estado_integridade(dados_atuais[5]),"dado": "integridade"},
        {"estado": estado_motor(dados_atuais[6]),"dado": "motor"},
    ]
    dados = Coluna([Texto("Infelizmente, você morreu"), Texto(""), Texto("estados criticos")])
    motivos = [Texto(f"{estado["dado"]}: {estado['estado'].name}") for estado in estados if estado["estado"] != Estado.ESTAVEL and estado["estado"] != Estado.MORTIFERO]
    dados.filhos.extend(motivos)
    dados.filhos.append(Texto(""))
    dados.filhos.append(Texto(f"causa da morte: {','.join(estado["dado"] for estado in estados if estado["estado"] == Estado.MORTIFERO)}"))
    while True:
        if estaPressionado("\n"):
            break
        
        print(
            Tabela(
                2,
                [
                    dados,
                    Coluna([AsciiAnimado("recursos/ascii/esqueleto.txt", i, 31)]),
                ],
            ).renderizar()
        )
        esperar(0.1)
        i += 1
        limpar()


def vitoria():
    i = 0
    while True:
        if estaPressionado("\n"):
            break
        print(
            Tabela(
                3,
                [
                    Coluna(
                        [
                            Texto("parabens, voce não morreu"),
                            AsciiAnimado("recursos/ascii/parabens.txt", i, 14),
                            
                            # , efeitos=[Cores1B.AZUL.value.efeito(CorAlvo.TEXTO)]
                        ]
                    ),
                    Coluna(
                        [
                            Ascii("recursos/ascii/dinheiro.txt"),
                            Coluna(
                                [
                                    Texto(f"{material.name}:{material.value.valor}")
                                    for material in banco_dados.asteroide.materiais
                                ]
                            ),
                        ]
                    ),
                    Coluna([Ascii("recursos/ascii/astronauta-inteiro.txt" , efeitos=[Cores1B.ROXO.value.efeito(CorAlvo.TEXTO)])]),
                    # , efeitos=[Cores1B.ROXO.value.efeito(CorAlvo.TEXTO)]
                ],
            ).renderizar()
        )
        esperar(0.25)
        i += 1
        limpar()
