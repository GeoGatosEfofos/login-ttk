import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Lógica de validação do login
    if username == "geo" and password == "spfc":
        messagebox.showinfo("Login", "ta certinho tlgd tmjt")
    else:
        messagebox.showerror("Login", "ta errado c de apto")

# Criar a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Definir a cor de fundo
root.configure(bg='pink')

# Configurar o layout
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.configure(style='TFrame')

# Adicionar estilo para o frame
style = ttk.Style()
style.configure('TFrame', background='pink')

# Labels e entradas
label_username = ttk.Label(frame, text="Usuário:", background='pink')
label_username.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entry_username = ttk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

label_password = ttk.Label(frame, text="Senha:", background='pink')
label_password.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Botão de login
button_login = ttk.Button(frame, text="Login", command=login)
button_login.grid(row=2, columnspan=2, pady=10)

# Iniciar o loop principal
root.mainloop()
