from tkinter import *
from PIL import ImageTk, Image  
import sqlite3
from tkinter import messagebox

ventana = Tk()
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.state('zoomed')
ventana.resizable(0, 0)
ventana.title('Inicio y registro')
# Logo usuario superior
icon = PhotoImage(file='images\\pic-icon.png')
ventana.iconphoto(True, icon)
PaginaLogin = Frame(ventana)
PaginaRegistro = Frame(ventana)
for frame in (PaginaLogin, PaginaRegistro):
    frame.grid(row=0, column=0, sticky='nsew')
def mostrar_frame(frame):
    frame.tkraise()
mostrar_frame(PaginaLogin)
#Variables de la base de datos
Email = StringVar()
Nombre = StringVar()
Contraseña = StringVar()
ConfirmarContraseña= StringVar()

#Pagina Login

disenio_frame1 = Listbox(PaginaLogin, bg='#0c71b9', width=500, height=100, highlightthickness=0, borderwidth=0)
disenio_frame1.place(x=0, y=0)

disenio_frame2 = Listbox(PaginaLogin, bg='#1e85d0', width=500, height=100, highlightthickness=0, borderwidth=0)
disenio_frame2.place(x=676, y=0)

disenio_frame3 = Listbox(PaginaLogin, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
disenio_frame3.place(x=75, y=106)

disenio_frame4 = Listbox(PaginaLogin, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
disenio_frame4.place(x=676, y=106)

# Entrada e-mail
entrada_email = Entry(disenio_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=Email)
entrada_email.place(x=134, y=170, width=256, height=34)
entrada_email.config(highlightbackground="black", highlightcolor="black")
etiqueta_email = Label(disenio_frame4, text='• Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
etiqueta_email.place(x=130, y=140)

#Entrada de la contraseña

contrasenia_entrada1 = Entry(disenio_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                        textvariable=Contraseña)
contrasenia_entrada1.place(x=134, y=250, width=256, height=34)
contrasenia_entrada1.config(highlightbackground="black", highlightcolor="black")
etiqueta_contrasenia= Label(disenio_frame4, text='• Contraseña', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
etiqueta_contrasenia.place(x=130, y=220)

# Esconder o mostrar la contraseña

def comando_contrasenia():
    if contrasenia_entrada1.cget('show') == '•':
        contrasenia_entrada1.config(show='')
    else:
        contrasenia_entrada1.config(show='•')

#Boton chequeo

boton_chequeo = Checkbutton(disenio_frame4, bg='#f8f8f8', command=comando_contrasenia, text='Mostrar contraseña')
boton_chequeo.place(x=140, y=288)

#Botones

boton_registro = Button(PaginaLogin, text='Registrarse', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: mostrar_frame(PaginaRegistro), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
boton_registro.place(x=1100, y=175)

#Etiqueta Bienvenida
etiqueta_bienvenido= Label(disenio_frame4, text='Bienvenido', font=('Arial', 18, 'bold'), bg='#f8f8f8')
etiqueta_bienvenido.place(x=130, y=13)

#Boton ingresar arriba
boton_login = Button(PaginaLogin, text='Ingresar', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', cursor='hand2')
boton_login.place(x=845, y=175)

linea_login = Canvas(PaginaLogin, width=60, height=5, bg='#1b87d2')
linea_login.place(x=850, y=203)

#Boton ingresar abajo

boton_login1= Button(disenio_frame4, fg='#f8f8f8', text='Ingresar', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=lambda: login())
boton_login1.place(x=133, y=340, width=256, height=50)

#Iconos

#Icono e-mail

icono_email = Image.open('images\\email-icon.png')
imagen = ImageTk.PhotoImage(icono_email)
etiqueta_imagen_email = Label(disenio_frame4, image=imagen, bg='#f8f8f8')
etiqueta_imagen_email.image = imagen
etiqueta_imagen_email.place(x=105, y=174)

#Icono contraseña

icono_contrasenia = Image.open('images\\pass-icon.png')
imagen = ImageTk.PhotoImage(icono_contrasenia)
etiqueta_icono_contrasenia= Label(disenio_frame4, image=imagen, bg='#f8f8f8')
etiqueta_icono_contrasenia.image = imagen
etiqueta_icono_contrasenia.place(x=105, y=254)

# icono imagen
icono_imagen= Image.open('images\\pic-icon.png')
imagen = ImageTk.PhotoImage(icono_imagen)
etiqueta_icono_imagen = Label(disenio_frame4, image=imagen, bg='#f8f8f8')
etiqueta_icono_imagen.image = imagen
etiqueta_icono_imagen.place(x=280, y=5)

# imagen izquierda
imagen_lado = Image.open('images\\super.png')
imagen = ImageTk.PhotoImage(imagen_lado)
etiqueta_imagen_lado = Label(disenio_frame3, image=imagen, bg='#1e85d0')
etiqueta_imagen_lado.image = imagen
etiqueta_imagen_lado.place(x=50, y=10)

#Login conexion base de datos
connection = sqlite3.connect('RegLog.db')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS RegLog(Email TEXT PRIMARY KEY, Nombre TEXT, Contraseña TEXT, "
            "ConfirmarContraseña TEXT)")
connection.commit()
connection.close()


def login():
    conn = sqlite3.connect("RegLog.db")
    cursor = conn.cursor()

    find_user = 'SELECT * FROM RegLog WHERE Email = ? and Contraseña = ?'
    cursor.execute(find_user, [(entrada_email.get()), (contrasenia_entrada1.get())])

    result = cursor.fetchall()
    if result:
        messagebox.showinfo("Éxito", 'Ingreso exitoso.')
    else:
        messagebox.showerror("Falla", "Datos de ingreso erroneos, por favor intente de nuevo.")


#olvido contraseña página


def contrasenia_olvidada():
    win = Toplevel()
    ventana_ancho = 350
    ventana_altura = 350
    pantalla_ancho = win.winfo_screenwidth()
    pantalla_altura = win.winfo_screenheight()
    posicion_top = int(pantalla_altura / 4 - ventana_altura / 4)
    posicion_derecha = int(pantalla_ancho / 2 - ventana_ancho / 2)
    win.geometry(f'{ventana_ancho}x{ventana_altura}+{posicion_derecha}+{posicion_top}')
    win.title('Contraseña olvidada')
    win.iconbitmap('images\\aa.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # Variables
    email = StringVar()
    password = StringVar()
    confirmarcontrasenia= StringVar()

    # email
    entrada_email2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                         textvariable=email)
    entrada_email2.place(x=40, y=30, width=256, height=34)
    entrada_email2.config(highlightbackground="black", highlightcolor="black")
    etiqueta_email2= Label(win, text='• Correo Electrónico', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    etiqueta_email2.place(x=40, y=0)

    # nueva contraseña
    entrada_nueva_contrasenia= Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                               textvariable=password)
    entrada_nueva_contrasenia.place(x=40, y=110, width=256, height=34)
    entrada_nueva_contrasenia.config(highlightbackground="black", highlightcolor="black")
    etiqueta_nueva_contrasenia = Label(win, text='• Nueva Contraseña', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    etiqueta_nueva_contrasenia.place(x=40, y=80)

    #Confirmar contraseña
    entrada_confirmar_contrasenia = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2
                                   , textvariable=confirmarcontrasenia)
    entrada_confirmar_contrasenia.place(x=40, y=190, width=256, height=34)
    entrada_confirmar_contrasenia.config(highlightbackground="black", highlightcolor="black")
    etiqueta_confirmar_contrasenia = Label(win, text='• Confirmar Contraseña', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    etiqueta_confirmar_contrasenia.place(x=40, y=160)

    # Boton actualizar contraseña
    actualizar_contrasenia = Button(win, fg='#f8f8f8', text='Actualizar Contraseña', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2', command=lambda: cambiar_contrasenia())
    actualizar_contrasenia.place(x=40, y=240, width=256, height=50)

    #Conexion base de datos para contraseña olvidada
    def cambiar_contrasenia():
        if entrada_nueva_contrasenia.get() == entrada_confirmar_contrasenia.get():
            db = sqlite3.connect("RegLog.db")
            curs = db.cursor()

            insert = '''update RegLog set Contraseña=?, ConfirmarContraseña=? where Email=? '''
            curs.execute(insert, [entrada_nueva_contrasenia.get(), entrada_confirmar_contrasenia.get(), entrada_email2.get(), ])
            db.commit()
            db.close()
            messagebox.showinfo('Éxito', 'Cambio de contraseña exitoso')

        else:
            messagebox.showerror('Error!', "Las contraseñas no coinciden")


contraseniaolvidada = Button(disenio_frame4, text='Contraseña olvidada', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=lambda: contrasenia_olvidada(), cursor="hand2")
contraseniaolvidada.place(x=290, y=290)

#Pagina Registro

disenio_frame5 = Listbox(PaginaRegistro, bg='#0c71b9', width=500, height=100, highlightthickness=0, borderwidth=0)
disenio_frame5.place(x=0, y=0)

disenio_frame6 = Listbox(PaginaRegistro, bg='#1e85d0', width=500, height=100, highlightthickness=0, borderwidth=0)
disenio_frame6.place(x=676, y=0)

disenio_frame7 = Listbox(PaginaRegistro, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
disenio_frame7.place(x=75, y=106)

disenio_frame8 = Listbox(PaginaRegistro, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
disenio_frame8.place(x=676, y=106)

#Nombre
entrada_nombre = Entry(disenio_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                   textvariable=Nombre)
entrada_nombre.place(x=284, y=150, width=286, height=34)
entrada_nombre.config(highlightbackground="black", highlightcolor="black")
etiqueta_nombre = Label(disenio_frame8, text='•Nombre', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
etiqueta_nombre.place(x=280, y=120)

#email
entrada_email = Entry(disenio_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                    textvariable=Email)
entrada_email.place(x=284, y=220, width=286, height=34)
entrada_email.config(highlightbackground="black", highlightcolor="black")
etiqueta_email = Label(disenio_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
etiqueta_email.place(x=280, y=190)

#Contraseña 

entrada_contrasenia = Entry(disenio_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,
                       textvariable=Contraseña)
entrada_contrasenia.place(x=284, y=295, width=286, height=34)
entrada_contrasenia.config(highlightbackground="black", highlightcolor="black")
etiqueta_contrasenia = Label(disenio_frame8, text='• Contraseña', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
etiqueta_contrasenia.place(x=280, y=265)


def comando_contrasenia2():
    if entrada_contrasenia.cget('show') == '•':
        entrada_contrasenia.config(show='')
    else:
        entrada_contrasenia.config(show='•')


boton_chequeo = Checkbutton(disenio_frame8, bg='#f8f8f8', command=comando_contrasenia2, text='mostrar contraseña')
boton_chequeo.place(x=290, y=330)


# Confirmar contraseña
confirmarcontrasenia_entrada = Entry(disenio_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,
                              textvariable=ConfirmarContraseña)
confirmarcontrasenia_entrada.place(x=284, y=385, width=286, height=34)
confirmarcontrasenia_entrada.config(highlightbackground="black", highlightcolor="black")
etiqueta_confirmarcontrasenia = Label(disenio_frame8, text='• Confirmar Contraseña', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
etiqueta_confirmarcontrasenia.place(x=280, y=355)

#Botones 

boton_registro = Button(PaginaRegistro, text='Registrarse', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: mostrar_frame(PaginaLogin), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
boton_registro.place(x=1100, y=175)

linea_registro = Canvas(PaginaRegistro, width=60, height=5, bg='#1b87d2')
linea_registro.place(x=1115, y=203)

#Etiqueta Bienvenido 

etiqueta_bienvenido = Label(disenio_frame8, text='Bienvenido', font=('Arial', 18, 'bold'), bg='#f8f8f8')
etiqueta_bienvenido.place(x=130, y=13)

# boton login

boton_login = Button(PaginaRegistro, text='Ingresar', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: mostrar_frame(PaginaLogin), cursor='hand2')
boton_login.place(x=845, y=175)

# boton registro abajo

registro2 = Button(disenio_frame8, fg='#f8f8f8', text='Registrarse', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2', command=lambda: subir())
registro2.place(x=285, y=435, width=286, height=50)

# Icono contraseña

icono_contrasenia = Image.open('images\\pass-icon.png')
imagen = ImageTk.PhotoImage(icono_contrasenia)
etiqueta_icono_contrasenia = Label(disenio_frame8, image=imagen, bg='#f8f8f8')
etiqueta_icono_contrasenia.image = imagen
etiqueta_icono_contrasenia.place(x=255, y=300)

#icono confirmar contraseña

icono_confirmarcontrasenia = Image.open('images\\pass-icon.png')
imagen = ImageTk.PhotoImage(icono_confirmarcontrasenia)
etiqueta_icono_confirmarcontrasenia = Label(disenio_frame8, image=imagen, bg='#f8f8f8')
etiqueta_icono_confirmarcontrasenia.image = imagen
etiqueta_icono_confirmarcontrasenia.place(x=255, y=390)

# icono email

icono_email = Image.open('images\\email-icon.png')
imagen = ImageTk.PhotoImage(icono_email)
etiqueta_icono_email = Label(disenio_frame8, image=imagen, bg='#f8f8f8')
etiqueta_icono_email.image = imagen
etiqueta_icono_email.place(x=255, y=225)

# Icono nombre

icono_nombre = Image.open('images\\name-icon.png')
imagen = ImageTk.PhotoImage(icono_nombre)
etiqueta_icono_nombre = Label(disenio_frame8, image=imagen, bg='#f8f8f8')
etiqueta_icono_nombre.image = imagen
etiqueta_icono_nombre.place(x=252, y=153)

#imagen icono

icono_imagen = Image.open('images\\pic-icon.png')
imagen = ImageTk.PhotoImage(icono_imagen)
etiqueta_icono_imagen = Label(disenio_frame8, image=imagen, bg='#f8f8f8')
etiqueta_icono_imagen.image = imagen
etiqueta_icono_imagen.place(x=280, y=5)

#Imagen izquierda

imagen_lado= Image.open('images\\super.png')
imagen = ImageTk.PhotoImage(imagen_lado)
imagen_lado_etiqueta = Label(disenio_frame7, image=imagen, bg='#1e85d0')
imagen_lado_etiqueta.image = imagen
imagen_lado_etiqueta.place(x=50, y=10)

#Conexion base de datos

connection = sqlite3.connect('RegLog.db')
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS RegLog(Email TEXT PRIMARY KEY, Nombre TEXT, Contraseña TEXT, "
            "ConfirmarContraseña TEXT)")
connection.commit()
connection.close()


def subir():
    contador = 0
    advertencia= ""
    if entrada_nombre.get() == "":
        advertencia= "El campo nombre no puede estar vacío"
    else:
        contador += 1

    if entrada_email.get() == "":
        advertencia= "El campo email no puede estar vacío"
    else:
        contador += 1

    if entrada_contrasenia.get() == "":
        advertencia= "El campo contraseña no puede estar vacío"
    else:
        contador += 1

    if confirmarcontrasenia_entrada.get() == "":
        advertencia= "Registro incorrecto,asegúrese de que todos los campos esten completos"
    else:
        contador += 1

    if entrada_contrasenia.get() != confirmarcontrasenia_entrada.get():
        advertencia= "Las contraseñas no coinciden!"
    else:
        contador += 1

    if contador == 5:
        try:
            connection = sqlite3.connect("RegLog.db")
            cur = connection.cursor()
            cur.execute("INSERT INTO RegLog values(?,?,?,?)",
                        (Email.get(), Nombre.get(), Contraseña.get(), ConfirmarContraseña.get()))

            connection.commit()
            connection.close()
            messagebox.showinfo("Éxito", "Nueva cuenta creada exitosamente")

        except Exception as e:
            messagebox.showerror('', e)
    else:
        messagebox.showerror('Error', advertencia)


ventana.mainloop()
