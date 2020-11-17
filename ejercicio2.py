"""
Ejercicio 2.

Generar una clase llamada Password que siga las siguientes condiciones

a.- Que tenga el atributo contraseña.

b.- Un metodo que se llame esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener más de 2 mayusculas, al menos un carácter especial , más de 5 números y más de 3 vocales .

            por ejemplo instanciando 

Password1= Password(“xldsld”)

Password1.esfuerte() """

from tkinter import *
from password import Password

# Creo la ventana
raiz = Tk()
# Le doy un titulo a la ventana
raiz.title("Tu Verificador de Password")

# Defino las variables y constantes
contraseña = StringVar()
resultado = StringVar()

# Defino las funciones
def verificarContra():
    password = Password(contraseña.get())
    
    if password.esFuerte():
        resultado.set("¡Contraseña Fuerte!")
    else:
        resultado.set("¡Contraseña Debil!")

# Defino el Frame
miFrame = Frame(raiz, bg="#76F163")
# Coloco en pantalla el frame y le digo que adapte su tamaño a la raiz
miFrame.pack(fill="both", expand="True")

contraLabel = Label(miFrame, text="Ingresar una contraseña porfavor")
# Defino su posición y le doy una distancia del contenido al contenedor
contraLabel.grid(row=0, column=0, pady=10, padx=10)
# Configuro el color de fondo del label
contraLabel.config(bg="#76F163")

dolarEntry = Entry(miFrame, textvariable=contraseña)
dolarEntry.grid(row=0, column=1, pady=10, padx=10)

boton = Button(miFrame, text="Verificar", command=verificarContra)
boton.grid(row=0, column=2, pady=10, padx=10)

# Defino una caja de texto para visualizar el resultado de la operación
resultadoLabel = Label(miFrame, textvariable=resultado, bg="#76F163", fg="red")
resultadoLabel.grid(row=1, column=0)

# Genero in ciclo infinito sobre la ventana
raiz.mainloop()