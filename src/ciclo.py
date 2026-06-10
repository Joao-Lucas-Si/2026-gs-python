import random
from typing import Text, TypedDict

from src.eventos import Evento, Eventos
from src.banco_dados import Estado, Parametro, Tendencia
from src.acoes import menuAcoes
from src.banco_dados import banco_dados
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

# from src.dados import dados_missao, dados_atuais, historico_tendencias


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


def cabecalho(ciclos = 0):
    print(
        Coluna(
            [
                Coluna(
                    [
                        Preencher("="),
                        Texto("MISSION CONTROL"),
                        Preencher("="),
                        Texto(
                            "Operação CosmosMiner"
                            + "\n"
                            + "Equipe: AstroTech"
                            # + "\n"
                             + (f"\nCiclos analisados: {ciclos}" if ciclos > 0 else "")
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
    pontos= f"({atual} pontos criticos)"
    if atual == estavel:
        return Texto(f"a nave esta em excelentes condições {pontos}")
    elif atual == total:
        return Texto(f"o sistema inteiro está comprometido {pontos}")
    elif atual > critico:
        return Texto(f"o sistema está quase comprometido {pontos}")
    elif atual > media:
        return Texto(f"o sistema está parcialmente comprometido {pontos}")
    elif atual > baixa:
        return Texto(f"a nave apresenta algumas falhas")
    else:
        return Texto(f"o sistema ainda está em condições aceitaveis (0 pontos criticos)")


def obter_situacao_comparativa():
    if len(banco_dados.rodada.tendencias) > 0:
        anterior = banco_dados.rodada.tendencias[-1]
        atual = [
            parametro.tendencia_atual.estado
            for parametro in banco_dados.rodada.parametros
        ]

        anterior_pontos = sum(list(map(lambda x: x.value, anterior)))
        atual_pontos = sum(map(lambda x: x.value, atual))
        comparacao = f"({atual_pontos} vs {anterior_pontos})"
        if anterior_pontos > atual_pontos:
            return Texto(
                f"esse ciclo apresenta uma melhora na condição em comparação ao anterior {comparacao}"
            )
        elif anterior_pontos < atual_pontos:
            return Texto(
                f"esse ciclo apresenta uma piora na condição em comparação ao anterior {comparacao}"
            )
        return Texto(
            f"quanto o ciclo atual quanto o anteiror apresentam a mesma condição {comparacao}"
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
    if evento:
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
            Opcao(Coluna([Texto("1. continuar?")]), nothing),
            Opcao(Coluna([Texto("2. abrir ações")]), menuAcoes),
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
                    ]
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
    rodada = banco_dados.rodada
    while rodada.tempo_atual <= rodada.tempo_final:
        limpar()
        if rodada.tempo_atual == 1:
            cabecalho()
        rodada.dados.append([parametro.valor for parametro in rodada.parametros])
        ciclo(rodada.tempo_atual)

        rodada.tendencias.append(
            [
                parametro.tendencia_atual.estado
                for parametro in banco_dados.rodada.parametros
            ]
        )
        for parametro in banco_dados.rodada.parametros:
            parametro.tendencia_atual.atividade += 1
            parametro.gerar_tendencia()

        for parametro in rodada.parametros:
            if (
                parametro.tendencia_atual.estado == Estado.CRITICO
                and parametro.tendencia_atual.atividade > 1
                and random.randint(0, 10) > 7
            ):
                rodada.morte = parametro.nome

        if rodada.morte:
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


def sumario():
    rodada = banco_dados.rodada
    # dados_missao = [[temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo]]
    dados_tabela: list[Elemento] = list(
        [
            Coluna([Texto("Temperatura")]),
            Coluna([Texto("Comunicação")]),
            Coluna([Texto("Bateria")]),
            Coluna([Texto("Oxigenio")]),
            Coluna([Texto("Estabilidade")]),
            Coluna([Texto("Integridade")]),
        ]
        + [Coluna([Texto(f"{x}")]) for dado in rodada.dados for x in dado]
    )
    estados_tabela: list[Elemento] = list(
        [
            Coluna([Texto("Temperatura")]),
            Coluna([Texto("Comunicação")]),
            Coluna([Texto("Bateria")]),
            Coluna([Texto("Oxigenio")]),
            Coluna([Texto("Estabilidade")]),
            Coluna([Texto("Integridade")]),
        ]
        + [Coluna([Texto(f"{x.name}")]) for dado in rodada.tendencias for x in dado]
    )
    print(Coluna([Texto("dados"), Tabela(6, dados_tabela)]).renderizar())
    print(Coluna([Texto("estados"), Tabela(6, estados_tabela)]).renderizar())


def derrota():
    rodada = banco_dados.rodada
    i = 0

    dados = Coluna(
        [Texto("Infelizmente, você morreu"), Texto(""), Texto("estados criticos")]
    )
    motivos = [
        Texto(f"{parametro.nome}: {parametro.tendencia_atual.estado.name}")
        for parametro in rodada.parametros
        if parametro.tendencia_atual.estado != Estado.ESTAVEL
    ]
    dados.filhos.extend(motivos)
    dados.filhos.append(Texto(""))
    dados.filhos.append(Texto(f"causa da morte: {rodada.morte}"))
    pressionado = InputTarefa()
    while True:
        cabecalho(banco_dados.rodada.tempo_atual)
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
    sumario()

def vitoria():
    i = 0
    pressionado = InputTarefa()
    while True:
        cabecalho(banco_dados.rodada.tempo_atual)
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
    sumario()
