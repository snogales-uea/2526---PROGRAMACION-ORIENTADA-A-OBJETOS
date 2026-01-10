# Registrar un estudiante y calcular sus notas

# entradas
nombre_estudiante = input("Ingresa tu nombre: ") # snake_case
edadEstudiante = int(input("Ingresa tu edad: ")) # camelCase

nota_parcial_1 = float(input("Ingresa nota parcial 1: ")) # snake_case
notaParcial2 = float(input("Ingresa nota parcial 2: ")) # camelCase

# procesamiento
def aprueba_estudiante(nota_parcial_1, nota_parcial_2):
    suma_notas = nota_parcial_1 + nota_parcial_2
    if suma_notas >= 70:
        print("El estudiante aprueba la POO.")
    elif suma_notas >= 40:
        print("El estudiante tiene que dar examen de recuperación.")
    else:
        print("El estudiante pierde la asignatura.")

# salida
print(f"El nombre del estudiante es {nombre_estudiante}")
print(f"Edad del estudiante es {edadEstudiante} años")
aprueba_estudiante(nota_parcial_1, notaParcial2)