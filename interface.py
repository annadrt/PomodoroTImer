import tkinter as tk
from pomodoro import rodar_sessao, rodar_pausa

root = tk.Tk()
root.geometry("600x400")
root.title("Pomodoro Timer")

def tick_pausa(tempo_restante, pausa, sessao):
    if tempo_restante > 0:
        print(f"Tempo da pausa: {pausa}")
        root.after(1000, lambda: tick(pausa -1))
        

def tick(tempo_restante, pausa, sessao, nomeSessoes, sessaoAtual):
    if tempo_restante > 0:
        print(f"Tempo restante:  {tempo_restante}")
        root.after(1000, lambda: tick(tempo_restante -1))
    else:
        print("Finish.")

def startFunction():
    duracao = int(entry_duracao.get())
    print(duracao)
    pausa = int(entry_pausa.get())
    print(pausa)
    sessao = int(entry_sessao.get())
    print(sessao)
    tick(duracao)
    


startButton = tk.Button(root, text ='Start.', command = startFunction)

duracao_label = tk.Label(root, text = 'Tempo da sessão: ')
entry_duracao = tk.Entry(root)

pausa_label = tk.Label(root, text = 'Tempo da pausa: ')
entry_pausa = tk.Entry(root)

sessao_label = tk.Label(root, text = 'Quantidade de sessões: ')
entry_sessao = tk.Entry(root)

duracao_label.pack()
pausa_label.pack()
sessao_label.pack()
entry_duracao.pack()
entry_pausa.pack()
entry_sessao.pack()
startButton.pack()


root.mainloop()