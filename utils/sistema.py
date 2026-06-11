import os
from threading import Thread
from time import sleep

# def takeinput():
#     stdin = open(0)
#     print("give it up:", end = "", flush = 1)
#     x = stdin.readline()
#     print(x)
# if __name__ == "__main__":
#     process = multiprocessing.Process(target = takeinput)
#     process.start()
#     time.sleep(5)
#     process.terminate()
#     process.join()
#     print("\nalright, times up!")




def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(tempo: float):
    sleep(tempo)

def pausar():
    input()
    limpar()    
