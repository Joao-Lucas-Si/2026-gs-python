import random
from typing import Text, TypedDict

from src.eventos import Evento, Eventos
from src.banco_dados import Estado, Parametro, Tendencia
from src.acoes import menuAcoes
from src.banco_dados import banco_dados
from src.recomendacao import (
    estado_bateria,
    estado_comunicacao,
    estado_estabilidade,
    estado_integridade,
    estado_oxigenio,
    estado_temperatura,
)
from utils.arquivos import Database
from utils.menu import Opcao, menu
from utils.sistema import InputTarefa, esperar, limpar, pausar

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
from src.dados import dados_missao, dados_atuais, historico_tendencias


def flat[T](lista: list[list[T]]):
    x: list[T] = []
    for sub in lista:
        x.extend(sub)
    return x


class ValorDado:
    valor: int | float = 2
    estado: str = "NORMAL"
    comentario: str = "ESTAVEL"

    def __init__(self, valor: float | int, estado: str, comentario: str) -> None:
        self.valor = valor
        self.estado = estado
        self.comentario = comentario


def ciclo_tabela(parametros: list[Parametro]) -> Elemento:
    return Tabela(
        3,
        flat(
            [
                [
                    Coluna([Texto(parametro.nome)]),
                    Coluna([Texto(f"{parametro.valor}")]),
                    Coluna([Texto(f"{parametro.tendencia_atual.estado.name}")]),
                    # Coluna([Texto(f"{parametro.tendencia_atual.recomendacao}")]),
                ]
                for parametro in parametros
            ]
        ),
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

def obter_evento():
    if random.randint(0, 10) > 9:
        
        eventos = Eventos.valores()
        evento = eventos[random.randint(0, len(eventos) - 1)]
        return evento.value

def mostrar_evento(evento: Evento):
    return Coluna(
        [
            Texto(""),
            Texto(f"evento: {evento.nome}"),
            Texto(evento.descricao),
        ]
    )


def obter_situacao():
    atual = sum(
        map(
            lambda x: x.value,
            [
                parametro.tendencia_atual.estado
                for parametro in banco_dados.rodada.parametros
            ],
        )
    )

    total = 6 * 2
    critico = int(total * 0.6)
    media = int(total * 0.4)
    baixa = int(total * 0.1)
    estavel = 0

    if atual == estavel:
        return Texto("a nave esta em excelentes condições")
    elif atual == total:
        return Texto("o sistema inteiro está comprometido")
    elif atual > critico:
        return Texto("o sistema está quase comprometido")
    elif atual > media:
        return Texto("o sistema está parcialmente comprometido")
    elif atual > baixa:
        return Texto("a nave apresenta algumas falhas")
    else:
        return Texto("o sistema ainda está em condições aceitaveis")


def obter_situacao_comparativa():
    if len(banco_dados.rodada.tendencias) > 0:
        anterior = banco_dados.rodada.tendencias[-1]
        atual = [
            parametro.tendencia_atual.estado
            for parametro in banco_dados.rodada.parametros
        ]

        anterior_pontos = sum(list(map(lambda x: x.value, anterior)))
        atual_pontos = sum(map(lambda x: x.value, atual))

        if anterior_pontos > atual_pontos:
            return Texto(
                "esse ciclo apresenta uma melhora na condição em comparação ao anterior"
            )
        elif anterior_pontos < atual_pontos:
            return Texto(
                "esse ciclo apresenta uma piora na condição em comparação ao anterior"
            )
        return Texto(
            "quanto o ciclo atual quanto o anteiror apresentam a mesma condição"
        )
    return Coluna([])


def ciclo(ciclos):
    def nothing():
        pass

    db = banco_dados
    rodada = db.rodada
    parametros = rodada.parametros
    esperar(0.5)
    evento = obter_evento()
    if (evento):
        evento.consequencia(rodada.parametros)
        for i, parametro in enumerate(rodada.parametros):
            rodada.dados_atuais[i] = parametro.valor
    perigos = [
        parametro
        for parametro in parametros
        if parametro.tendencia_atual.estado != Estado.ESTAVEL
    ]
    menu(
        "Relatorio ciclo",
        [
            Opcao(Coluna([Texto("continuar?")]), nothing),
            Opcao(Coluna([Texto("abrir ações")]), menuAcoes),
        ],
        colunas=2,
        top=lambda: Coluna(
            [
                Tabela(
                    2,
                    [
                        Coluna(
                            [
                                Texto(f"Ciclo {ciclos}"),
                                ciclo_tabela(parametros),
                            ]
                        ),
                        Coluna([Ascii("recursos/ascii/naves/foguete_medio.txt")]),
                    ],
                ),
                Coluna(
                    [Texto("Situação"), obter_situacao(), obter_situacao_comparativa()],
                ),
                (
                    Coluna([Texto("recomendações"), Texto("")])
                    if len(perigos)
                    else Coluna([])
                ),
                Coluna(
                    [
                        Texto(f" - {parametro.tendencia_atual.recomendacao}")
                        for parametro in perigos
                    ]
                ),
                mostrar_evento(evento) if evento != None else Coluna([]),
            ]
        ),
    )


# recursos/ascii/naves/foguete_medio.txt
def gerenciar_ciclo():

    while banco_dados.rodada.tempo_atual < banco_dados.rodada.tempo_final:
        limpar()
        if banco_dados.rodada.tempo_atual == 1:
            cabecalho(banco_dados.rodada.tempo_atual)
        banco_dados.rodada.dados.append(
            [parametro.valor for parametro in banco_dados.rodada.parametros]
        )
        ciclo(banco_dados.rodada.tempo_atual)

        historico_tendencias.append(
            [
                parametro.tendencia_atual.estado
                for parametro in banco_dados.rodada.parametros
            ]
        )
        for parametro in banco_dados.rodada.parametros:
            parametro.tendencia_atual.atividade += 1
            parametro.gerar_tendencia()
            

        if (
            estado_temperatura(dados_atuais[0]) == Estado.MORTIFERO
            or estado_comunicacao(dados_atuais[1]) == Estado.MORTIFERO
            or estado_bateria(dados_atuais[2]) == Estado.MORTIFERO
            or estado_oxigenio(dados_atuais[3]) == Estado.MORTIFERO
            or estado_estabilidade(dados_atuais[4]) == Estado.MORTIFERO
            or estado_integridade(dados_atuais[5]) == Estado.MORTIFERO
        ):
            break
        banco_dados.rodada.tempo_atual += 1

    if banco_dados.rodada.tempo_atual < banco_dados.rodada.tempo_final:
        derrota()
    else:
        banco_dados.pontos += sum(
            map(
                lambda material: material.value.valor,
                banco_dados.rodada.asteroide.materiais,
            )
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
        {"estado": estado_bateria(dados_atuais[2]), "dado": "bateria"},
        {"estado": estado_oxigenio(dados_atuais[3]), "dado": "oxigenio"},
        {"estado": estado_estabilidade(dados_atuais[4]), "dado": "estabilidade"},
        {"estado": estado_integridade(dados_atuais[5]), "dado": "integridade"},
    ]
    dados = Coluna(
        [Texto("Infelizmente, você morreu"), Texto(""), Texto("estados criticos")]
    )
    motivos = [
        Texto(f"{estado["dado"]}: {estado['estado'].name}")
        for estado in estados
        if estado["estado"] != Estado.ESTAVEL and estado["estado"] != Estado.MORTIFERO
    ]
    dados.filhos.extend(motivos)
    dados.filhos.append(Texto(""))
    dados.filhos.append(
        Texto(
            f"causa da morte: {','.join(estado["dado"] for estado in estados if estado["estado"] == Estado.MORTIFERO)}"
        )
    )
    pressionado = InputTarefa()
    while True:

        print(
            Tabela(
                2,
                [
                    dados,
                    Coluna([AsciiAnimado("recursos/ascii/esqueleto.txt", i, 31)]),
                ],
            ).renderizar()
        )
        pressionado.iniciar()
        if pressionado.pressionado:
            break
        esperar(0.1)
        i += 1
        limpar()
        pressionado.terminar()


def vitoria():
    i = 0
    pressionado = InputTarefa()
    while True:
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
                                    for material in banco_dados.rodada.asteroide.materiais
                                ]
                            ),
                        ]
                    ),
                    Coluna(
                        [
                            Ascii(
                                "recursos/ascii/astronauta-inteiro.txt",
                                efeitos=[Cores1B.ROXO.value.efeito(CorAlvo.TEXTO)],
                            )
                        ]
                    ),
                    # , efeitos=[Cores1B.ROXO.value.efeito(CorAlvo.TEXTO)]
                ],
            ).renderizar()
        )
        pressionado.iniciar()

        if pressionado.pressionado:
            break
        esperar(0.25)
        pressionado.terminar()
        i += 1
        limpar()
