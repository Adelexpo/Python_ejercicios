
class Vehiculo:
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = "Negro"
        self.Ruedas = 4
        self.Puertas = 5

v = Vehiculo("Negro", 4, 5)
print(v.Color)
print(v.Ruedas)
print(v.Puertas)

class Coche(Vehiculo):
    def __init__(self, Velucidad, Celindrada):
        self.Velucidad = 120
        self.Celindrada = 2000

c = Coche(120, 2000)
print(c.Velucidad)
print(c.Celindrada)



