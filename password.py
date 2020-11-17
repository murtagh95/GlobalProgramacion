"""
Ejercicio 2.

Generar una clase llamada Password que siga las siguientes condiciones

a.- Que tenga el atributo contraseña.

b.- Un metodo que se llame esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener más de 2 mayusculas, al menos un carácter especial , más de 5 números y más de 3 vocales .

            por ejemplo instanciando 

Password1= Password(“xldsld”)

Password1.esfuerte() """
import re


class Password():
    def __init__(self, contraseña):
        self.contraseña = contraseña
    
    def esFuerte(self):
        buscarMayus = re.findall("[A-Z]", self.contraseña)
        
        if len(buscarMayus) > 2:  # Si hay más de 2 mayus entonces:
            # Busco si se ha ingresado un caracter especial
            buscarCarEspe = re.findall("[^a-zA-Z0-9\s]", self.contraseña)
            if len(buscarCarEspe) > 0:  
                # Busco los números en la cadena
                buscarNumeros = re.findall("\d", self.contraseña)
                if len(buscarNumeros) > 5:
                    buscarVocales = re.findall("[aeiouAEIOU]",  self.contraseña)
                    if len(buscarVocales) > 3:
                        return True
        
        return False

            


# pas = Password("aaaaaaa")
# print(pas.esFuerte())

# pas1 = Password("AAaaaaaa   aslndas11Q")
# print(pas1.esFuerte())

# pas2 = Password("AA   eslndious111111Q/*")
# print(pas2.esFuerte())
