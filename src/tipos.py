



from enum import Enum


class Material():
    valor: int
    nome: str

    def __init__(self, nome: str, valor: int) -> None:
        self.nome = nome
        self.valor = valor


class Materiais(Enum):
    FERRO=Material("ferro", 10)
    Iridio=Material("iridio", 100)
    Silicatos=Material("silicatos", 50)
    Niquel=Material("niquel", 20)
    Cobalto=Material("cobalto", 30)
    Rodio=Material("rodio", 80)
    Paladio=Material("paladio", 150)
    Platina=Material("platina", 200)


class Asteroide():
    materiais: list[Materiais]
    nome: str
    tempo: int
    def __init__(self, materiais: list[Materiais], nome: str, tempo: int) -> None:
        self.materiais = materiais
        self.nome = nome
        self.tempo = tempo