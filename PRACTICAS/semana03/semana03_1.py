# ------------------ CLASE DIA DE CLIMA ------------------

class DiaClima:
    """
    Representa un día específico con su temperatura.
    Aplica encapsulamiento usando atributos privados.
    """
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura

    def mostrar_info(self):
        """Muestra la información del día y su temperatura."""
        print(f"{self.__dia}: {self.__temperatura}°C")

    def obtener_temperatura(self):
        """Devuelve la temperatura del día."""
        return self.__temperatura

# ------------------ CLASE SEMANA DE CLIMA ------------------

class SemanaClima:
    """
    Contiene una lista de objetos DiaClima y permite operar sobre ellos.
    Usa herencia para ser extendida por una subclase.
    """
    def __init__(self):
        self._dias = []  # Atributo protegido

    def agregar_dia(self, dia_clima):
        """Agrega un objeto DiaClima a la lista de la semana."""
        if isinstance(dia_clima, DiaClima):
            self._dias.append(dia_clima)

    def mostrar_todas(self):
        """Muestra todas las temperaturas registradas."""
        print("\nTemperaturas registradas durante la semana:")
        for dia in self._dias:
            dia.mostrar_info()

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas semanales."""
        if not self._dias:
            return 0
        total = sum(dia.obtener_temperatura() for dia in self._dias)
        return total / len(self._dias)


# ------------------ CLASE DETALLADA CON POLIMORFISMO ------------------

class SemanaClimaDetallada(SemanaClima):
    """
    Hereda de SemanaClima y extiende el comportamiento con un resumen.
    Aplica polimorfismo redefiniendo métodos.
    """
    def mostrar_resumen(self):
        """Muestra todas las temperaturas y el promedio."""
        self.mostrar_todas()
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal de temperatura: {promedio:.2f}°C")


# ------------------ PROGRAMA PRINCIPAL ------------------

# Lista de los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear instancia de la clase hija que extiende funcionalidad
semana = SemanaClimaDetallada()

# Recolectar datos del usuario
for dia in dias_semana:
    while True:
        try:
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            semana.agregar_dia(DiaClima(dia, temp))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Mostrar resultados
print("\n===== RESUMEN SEMANAL =====")
semana.mostrar_resumen()
