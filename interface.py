import tkinter as tk
from pomodoro import rodar_sessao, rodar_pausa

root = tk.Tk()
root.geometry("600x400")
root.title("Pomodoro Timer")

def tick_pausa(tempo_restante, pausa, sessao, duracao, nomeSessoes, sessaoAtual):
    if tempo_restante > 0:
        timer_var.set(f"{tempo_restante}")
        root.after(1000, lambda: tick_pausa(tempo_restante - 1, pausa, sessao, duracao, nomeSessoes, sessaoAtual))
    else:
        tick(duracao, duracao, pausa, sessao, nomeSessoes, sessaoAtual +1)
        

def tick(tempo_restante, duracao, pausa, sessao, nomeSessoes, sessaoAtual):
    if tempo_restante > 0:
        timer_var.set(f"{tempo_restante}")
        root.after(1000, lambda: tick(tempo_restante -1, duracao, pausa, sessao, nomeSessoes, sessaoAtual))
    else:
        if sessaoAtual < sessao:
            tick_pausa(pausa, pausa, sessao, duracao, nomeSessoes, sessaoAtual)
        else:
            timer_var.set("Finalizado!")

def startFunction():
    nomeSessoes = ['Sessão 1', "Sessão 2"]
    duracao = int(entry_duracao.get())
    print(duracao)
    pausa = int(entry_pausa.get())
    print(pausa)
    sessao = int(entry_sessao.get())
    print(sessao)
    tick(duracao, duracao, pausa, sessao, nomeSessoes, 1)
    

timer_var = tk.StringVar()
timer_label = tk.Label(root, textvariable = timer_var)
timer_var.set("10:00")


settingsButton = tk.Button(root, text = 'Settings')
startButton = tk.Button(root, text ='Start.', command = startFunction)

duracao_label = tk.Label(root, text = 'Tempo da sessão: ')
entry_duracao = tk.Entry(root)

pausa_label = tk.Label(root, text = 'Tempo da pausa: ')
entry_pausa = tk.Entry(root)

sessao_label = tk.Label(root, text = 'Quantidade de sessões: ')
entry_sessao = tk.Entry(root)

timer_label.pack()
duracao_label.pack()
pausa_label.pack()
sessao_label.pack()
entry_duracao.pack()
entry_pausa.pack()
entry_sessao.pack()
settingsButton.pack()
startButton.pack()


root.mainloop()