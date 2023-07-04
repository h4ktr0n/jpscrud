
from tkinter import ttk

entry = ttk.Entry()

def imprimir_texto():
 print(entry.get())

def main():
    
    entry.place(x=10, y=10)
    boton = ttk.Button(text="Imprimir texto", command=imprimir_texto)
    boton.place(x=10, y=50)

if __name__ == '__gui__':
   main()