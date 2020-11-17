from empleado import Empleado
from random import choice, randint


# DEFINO CONSTANTES
NOMBRES = (
	"Nicolas",
	"Jose",
	"Manuel",
	"Francisco",
	"Ciro",
	"Maria",
	"Noemi",
	"Lucia",
	"Teresa",
	"Natalia",
	"Camila",
	"Thalia",
	"Alexis",
	"Sol",
	"Lucrecio"
)
APELLIDOS =(
	"Catalano",
	"Salimeni",
	"Coria",
	"Figueroa",
	"Muratore",
	"Ortiz",
	"Perez",
	"Gonzales",
	"Matus",
	"Perez",
	"Echegaray",
	"Gomez",
	"Ruiz",
	"Manna",
	"Brizuela"
)
SEXO = ("Masculino", "Femenino", "No especificado")
EMPLEADOS = 100


class Empresa():
    
    def __init__(self, empleados = []):
        self.empleados = empleados

    def generarEmpleados(self):
        self.empleados.append(Empleado(
                choice(NOMBRES) + " " + choice(APELLIDOS),
                randint(16, 70),
                choice(SEXO),
                randint(14000, 40000)
            ))

    def buscarMenores18(self, sexo = None):
        """Genero un array con los objetos que tengan el atributo edad menor a 21"""
        if sexo == None:
            menores = filter(lambda empleado: empleado.edad < 18, self.empleados)        
        else:
            menores = filter(lambda empleado: empleado.edad < 18 and empleado.sexo == sexo, self.empleados)
        return menores
    
    def buscarMayores65(self, sexo = None):
        """Genero un array con los objetos que tengan el atributo edad mayor a 65"""
        if sexo == None:
            mayores = filter(lambda empleado: empleado.edad > 65, self.empleados)
        else:
            mayores = filter(lambda empleado: empleado.edad > 65 and empleado.sexo == sexo, self.empleados)
        return mayores
        
    def buscarMayorSueldo(self):
        listaSueldos = []

        # Agrego todos los sueldos en un arrey
        for empleado in self.empleados:
            listaSueldos.append(empleado.sueldoAnual)

        sueldoMax = max(listaSueldos)
        # Si se encuentra solo un empleado con el sueldo max
        if listaSueldos.count(sueldoMax) == 1:
            # Devuelvo un array con el empleado con mayor sueldo
            return [self.empleados[listaSueldos.index(sueldoMax)]]
        else:
            devolver = []
            # Recorro los empleados para devolver todos los que tengan sueldo MAX
            for empleado in self.empleados:
                if empleado.sueldoAnual == sueldoMax:
                    devolver.append(empleado)
            return devolver
        