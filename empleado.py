
class Persona():
    """
    Clase abstracta
    """
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class Empleado(Persona):
    def __init__(self, nombre, edad, sexo, sueldo):
        super().__init__(nombre, edad, sexo)
        self.sueldo = sueldo
        self.sueldoAnual = self.calcularSueldoAnual()

    def calcularSueldoAnual(self):
        return self.sueldo * 12
    
    def __str__(self):
        return "\tEmpleado: {}.\n\tEdad: {}.\n\tSexo: {}.\n\tSueldo: {}".format(
            self.nombre,
            self.edad,
            self.sexo,
            self.sueldo,
        )
