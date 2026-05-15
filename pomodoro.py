import time

def rodar_sessao(duracao, nomeSessoes, sessao):
    print(f"Sessão {sessao}: {nomeSessoes}")
    for i in range(duracao, -1, -1):
        time.sleep(1)
        print(f"Tempo restante: {i}")

def rodar_pausa(pausa, nomeSessoes):
    print(f"Próxima sessão: {nomeSessoes}")

    for k in range (pausa, -1, -1):
        time.sleep(1)
        print(f"Pausa: {k}")

def pedir_numero(mensagem):

    while True:
        try:

            valor = int(input(mensagem))
            break
        except ValueError:
            print ("Digite um número.")

    return valor


if __name__ == "__main__":

    duracao = pedir_numero("Tempo da sessão: ")
    pausa =  pedir_numero("Tempo da pausa: ")
    sessao = pedir_numero("Sessões: ")
    nomeSessoes = []

for i in range(sessao):
    nome = input(f"Nome da sessão {i+1}: ")
    nomeSessoes.append(nome)

for i in range(1, sessao + 1):
    rodar_sessao(duracao, nomeSessoes[i-1], i)

    if i < sessao:
        rodar_pausa(pausa, nomeSessoes[i])
    else:
        print("Finalizado.")