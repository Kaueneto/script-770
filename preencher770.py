import pyautogui
import time
import tkinter as tk
from tkinter import ttk

pyautogui.PAUSE = 0  # Sem delay entre ações

def executar_preenchimento(servico, repeticoes):
    for _ in range(repeticoes):
        pyautogui.write(servico)
        pyautogui.press('enter')
        pyautogui.press('down')

def iniciar_contagem():
    try:
        servico = combo_servico.get()
        repeticoes = int(entry_repeticoes.get())

        if not servico or servico not in ["20", "22", "30", "99"]:
            raise ValueError
        if repeticoes <= 0:
            raise ValueError

        # Desabilita os campos e botão
        entry_repeticoes.config(state="disabled")
        combo_servico.config(state="disabled")
        btn_iniciar.config(state="disabled")

        # Inicia contagem regressiva visual
        contagem_regressiva(servico, repeticoes, 5)

    except:
        label_status.config(text="Preencha todos os campos corretamente.", fg="red")

def contagem_regressiva(servico, repeticoes, segundos):
    if segundos > 0:
        label_status.config(text=f"Clique sobre o registro\nna rotina 770, Iniciando em: {segundos}...", fg="red")
        root.after(1000, contagem_regressiva, servico, repeticoes, segundos - 1)
    else:
        label_status.config(text="Executando...", fg="green")
        root.after(100, lambda: executar_e_finalizar(servico, repeticoes))

def executar_e_finalizar(servico, repeticoes):
    executar_preenchimento(servico, repeticoes)
    label_status.config(text="Finalizado!", fg="blue")
    btn_iniciar.config(state="normal")
    entry_repeticoes.config(state="normal")
    combo_servico.config(state="readonly")

# Interface
root = tk.Tk()
root.title("Preenchimento Automático 770")
root.geometry("300x230")
root.resizable(False, False)

tk.Label(root, text="Número de repetições:").pack(pady=(15, 5))
entry_repeticoes = tk.Entry(root)
entry_repeticoes.pack()

tk.Label(root, text="Tipo de serviço:").pack(pady=(10, 5))
combo_servico = ttk.Combobox(root, values=["20", "22", "30", "99"], state="readonly")
combo_servico.pack()

btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar_contagem)
btn_iniciar.pack(pady=20)

label_status = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_status.pack()

root.mainloop()
