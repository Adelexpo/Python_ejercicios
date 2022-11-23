class Alumno:
    def __init__(self, Nombre, Nota):
        self.Nombre = "Carlos"
        self.Nota = 8

n = 8
s = 4


a = Alumno("Carlos", 8)
print(a.Nombre)
print(a.Nota)

if n > s:
    print("Ha aprobado")
else:
    print("No ha aprobado")