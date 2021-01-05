class Prota:
    def __init__(self, nombre, edad, sexo, contextura, fisico):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.contextura = contextura
        self.fisico = fisico
        
    def Presentar(self):
        
        print("\n")
        print("Los atributos elegidos te otorgaran los siguientes stats para tu personaje: ")
        print("\n")
        print("Nombre: " + self.nombre + "\n" + "Edad: " + str(self.edad) +"\n" +"Sexo: " + self.sexo)

        
class Stats_iniciales:
    def __init__(self, fuerza, velocidad, hambre, salud):
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.hambre = hambre
        self.salud = salud
        
    def Mostrar_stat_iniciales(self):
        
        print("Fuerza: " + str(self.fuerza))
        print("Velocidad: " + str(self.velocidad))
        print("Hambre: " + str(self.hambre))
        print("Salud: " + str(self.salud))