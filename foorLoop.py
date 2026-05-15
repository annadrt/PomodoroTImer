import time

duracao = 10
sessao = int(input(""))
pausa = int(input(""))

for i in range(1, sessao + 1):
    print(f"Sessão atual: {i}")
    
    for j in range(duracao, -1, -1):
            time.sleep(1)
            print(f"Tempo restante: {j} segundos")
    
    if i < sessao:
                  
        for k in range(pausa, -1, -1):
            time.sleep(1)
            print(f"Pausa: {k}")
    
    if i == sessao:
          print("Finalizado!")