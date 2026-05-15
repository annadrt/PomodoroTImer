import time

def rodar_sessao(duracao):
    for j in range(duracao, -1, -1):
            time.sleep(1)
            print(f"Tempo restante: {j} segundos")

rodar_sessao(10)

def rodar_pausa(pausa):
      for k in range (pausa, -1, -1):
            time.sleep(1)
            print(f"Pausa: {k}")

rodar_pausa(5)