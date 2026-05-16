import tkinter as tk

def sessionSettings():
    duracao = duracao.get()
    pausa = pausa.get()
    sessao = sessao.get()

    print("Tempo da sessão: " + duracao)
    print("Tempo da pausa: " + pausa)
    print("Número de sessões:" + sessao)

root = tk.Tk()
root.geometry("600x400")
root.title("Pomodoro Timer")


startButton = tk.Button(root, text ='Start.', command = sessionSettings)

entry_duracao = tk.Entry(root)
entry_pausa = tk.Entry(root)
entry_sessao = tk.Entry(root)

entry_duracao.pack()
entry_pausa.pack()
entry_sessao.pack()
startButton.pack()


root.mainloop()