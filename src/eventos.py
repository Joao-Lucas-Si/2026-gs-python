# aliens (+materia desconhecido ou -materiasi)
# entrada de vacuo (-oxigenio, -temperatura motor, e -temperatura)
# chuva de meteoro (-integridade)
# vazamento de combustivel (-bateria)
# interferencia de radio (-comunicacao)


from enum import Enum
from typing import Callable

from h11 import Event

from src.banco_dados import Estado, Parametro


class Evento:
    descricao: str
    nome: str
    consequencia: Callable[[list[Parametro]], None]

    def __init__(
        self, nome: str, descricao: str, consequencia: Callable[[list[Parametro]], None]
    ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.consequencia = consequencia
# [temperatura, comunicacao, bateria, oxigenio, estabilidade, integridade_modulo]
def aplicar_vacuo(parametros: list[Parametro]):
    parametros[0].definir_tendencia(Estado.CRITICO)
    parametros[0].tendencia_atual.duracao = 5
    parametros[3].definir_tendencia(Estado.CRITICO)
    parametros[3].tendencia_atual.duracao = 5

def aplicar_meteoro(parametros: list[Parametro]):
    parametros[5].definir_tendencia(Estado.CRITICO)
    parametros[5].tendencia_atual.duracao = 5

def aplicar_vazamento(parametros: list[Parametro]):
    parametros[2].definir_tendencia(Estado.CRITICO)
    parametros[2].tendencia_atual.duracao = 5

def aplicar_interferencia(parametros: list[Parametro]):
    parametros[1].definir_tendencia(Estado.CRITICO)
    parametros[1].tendencia_atual.duracao = 5


class Eventos(Enum):
    @staticmethod
    def valores():

        return list(Eventos)

    ENTRADA_VACUO = Evento(
        "entrada de vacuo",
        "devido a um defeito na nave houve uma pequena abertura para o vacuo, perdando oxigenio e baixando a temperatura",
        aplicar_vacuo,
    )
    CHUVA_METEORO = Evento(
        "Chuva de meteoros",
        "ocorreu uma chuva de meteoros durante sua trajetoria, partes da nave foram quebradas",
        aplicar_meteoro,
    )

    VAZAMENTO_COMBUSTIVEL = Evento(
        "vazamento de combustivel",
        "ocorreu um vazamento de combustivel, parte de sua bateria foi perdida",
        aplicar_vazamento,
    )

    INTERFERENCIA_RADIO = Evento(
        "interferencia de radio",
        "o radio de comunicação foi afetado por uma interferencia desconhecida, perdendo o contato com a base",
        aplicar_interferencia,
    )
