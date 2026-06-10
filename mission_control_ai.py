
from src.acoes import menuAcoes
from src.ciclo import ciclo, ciclo_tabela
from src.creditos import mostrarIntegrantes, mostrarLogo
from src.missao import menuMissao
from src.recomendacao import recomendacao_motor
from utils.tui.animacao import animarEscrita
from utils.tui.render.elementos import Ascii, Coluna, Tabela, Texto

def main():
    # mostrarLogo()
    # mostrarIntegrantes()
    print("aa")
    menuMissao()
    #menuAcoes()
    #ciclo(1)
    pass

if __name__ == "__main__":
    recomendacoes = ["Comunicao", "Energia", "Temperatura"]


    main()
