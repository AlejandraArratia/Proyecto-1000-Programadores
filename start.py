from tkinter import *
from tkinter.ttk import Progressbar
import sys

import os
root = Tk()
imagen = PhotoImage(file='images1\\imagen2.png')
altura= 470
ancho = 530
x = (root.winfo_screenwidth()//2)-(ancho//2)
y = (root.winfo_screenheight()//2)-(altura//2)
root.geometry('{}x{}+{}+{}'.format(ancho, altura, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='bisque2')
etiqueta_bienvenida = Label(text='Bienvenido a Supermark', bg='bisque2', font=("Gabriola", 40, "bold"), fg='black')
etiqueta_bienvenida.place(x=60, y=15)
etiqueta = Label(root, image=imagen, bg='bisque2')
etiqueta.place(x=135, y=110)
etiqueta_progreso = Label(root, text="Por favor espere...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='bisque2')
etiqueta_progreso.place(x=175, y=370)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=420)
boton_salida = Button(text='x', bg='bisque2', command=lambda: ventana_salida(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
boton_salida.place(x=490, y=0)
def ventana_salida():
    sys.exit(root.destroy())
def top():
    root.withdraw()
    os.system("python SistemaCuenta.py")
    root.destroy()
i = 0
def carga():
    global i
    if i <= 10:
        txt = 'Por favor espere...  ' + (str(10*i)+'%')
        etiqueta_progreso.config(text=txt)
        etiqueta_progreso.after(1000, carga)
        progress['value'] = 10*i
        i += 1
    else:
        top()
carga()
carga()
root.mainloop()