""" Ejercicio 1.

Dado una cantidad de información de empleados (dni, nombre, edad, sexo y sueldo neto mensual) escriba el código Python orientado a objetos que permita establecer

a.- Cuantos empleados son menores de 18 años.

b.- Cuantas empleadas(mujeres) son mayores de 65 años

c.- Cual(es) empleados tienen el mayor sueldo neto anual
"""
from empresa import Empresa, EMPLEADOS
from empleado import Empleado



# FUNCIONES
def eleguirSiSeguir():
    while True:
        print("Desea continuar(Y/N):")
        try:
            valor = input(">").lower()
            print(valor)
            if valor != "y" and valor != "n":
                print("----ERROR----")
                continue 
            return valor
        except:
            print("----ERROR----")
        
def eleguirSexo():
    while True:
        print("\t\tEleguir sobre quien realizar la busqueda:")
        print("\t1. Sexo Masculino")
        print("\t2. Sexo Femenino")
        print("\t3. Sexo no especificado")
        print("\t4. Todos")
        try:
            valor = int(input(">"))
            if valor < 1 or valor > 4:
                print("----ERROR----")
                continue 
            return valor
        except:
            print("----ERROR----")
            print("Ingresar el Nº de la opción elegida")

# Objetos creados para probar la busqueda del mayor sueldo
emp1 = Empleado("Nicolas", 22, "Masculino", 66)
emp2 = Empleado("Emanuel", 22, "Masculino", 55)

# Instancio la clase Empresa
empresa = Empresa([emp1, emp2])

# Genero 10 empleados
for _ in range(EMPLEADOS):
    empresa.generarEmpleados()


# GENERO EL MENU
while True:
    print("\t\t----------------------MENU----------------------")
    print("Eligue una opción(escribir solo el nº):")
    print("\t1. Ver empleados")
    print("\t2. Ver empleados menores a 18")
    print("\t3. Ver empleados mayores a 65")
    print("\t4. Ver empleados con mayor sueldo")
    print("\t5. Salir")
    try:
        opcion = int(input(">"))
        # ---------------------- OPCION 1 ----------------------
        if opcion == 1:
            print("Empleados:")
            for empleado in empresa.empleados:
                print(empleado)
                print("------------------------------------")
            
            # VERIFICO SI EL USUARIO QUIERE CONTINUAR
            op = eleguirSiSeguir()
            if(op == "n"):
                break

        # ---------------------- OPCION 2 ----------------------
        elif opcion == 2:
            valor = eleguirSexo()
            if valor == 1:
                print("Menores de 18 Masculinos:")
                menores = empresa.buscarMenores18("Masculino")
            elif valor == 2:
                print("Menores de 18 Femeninos:")
                menores = empresa.buscarMenores18("Femenino")
            elif valor == 3:
                print("Menores de 18 No especificado:")
                menores = empresa.buscarMenores18("No especificado")
            else:
                print("Menores de 18:")
                menores = empresa.buscarMenores18()
            
            
            for menor in menores:
                print(menor)
                print("------------------------------------")

            # VERIFICO SI EL USUARIO QUIERE CONTINUAR
            op = eleguirSiSeguir()
            if(op == "n"):
                break

        # ---------------------- OPCION 3 ----------------------
        elif opcion == 3:
            valor = eleguirSexo()
            if valor == 1:
                print("Mayores de 65 Masculinos:")
                mayores = empresa.buscarMayores65("Masculino")
            elif valor == 2:
                print("Mayores de 65 Femeninos:")
                mayores = empresa.buscarMayores65("Femenino")
            elif valor == 3:
                print("Mayores de 65 No especificado:")
                mayores = empresa.buscarMayores65("No especificado")
            else:
                print("Mayores de 65:")
                mayores = empresa.buscarMayores65()

            
            for mayor in mayores:
                print(mayor)
                print("------------------------------------")

            # VERIFICO SI EL USUARIO QUIERE CONTINUAR
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        
        # ---------------------- OPCION 4 ----------------------
        elif opcion == 4 :
            mayorSueldo = empresa.buscarMayorSueldo()
            print("Hay {} empleados con el sueldo más alto:".format(len(mayorSueldo)))
            for empleado in mayorSueldo:
                print(empleado)
                print("------------------------------------")
            
            # VERIFICO SI EL USUARIO QUIERE CONTINUAR
            op = eleguirSiSeguir()
            if(op == "n"):
                break
        
        # ---------------------- OPCION 5 ----------------------
        else:
            # SALGO DEL PROGRAMA
            break

    except:
        print("----------ERROR----------")
        print("Ingresar un número entero")


