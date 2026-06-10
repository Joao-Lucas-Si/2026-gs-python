
from src.acoes import menuAcoes
from src.ciclo import ciclo, ciclo_tabela
from src.creditos import mostrarIntegrantes, mostrarLogo
from src.missao import menuMissao
from utils.tui.animacao import animarEscrita
from utils.tui.render.elementos import Ascii, Coluna, Tabela, Texto

def main():
    menuMissao()

if __name__ == "__main__":
    main()
