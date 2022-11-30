import sqlite3

conexion = sqlite3.connect('Alumnos.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios con nombres, edades y emails
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos " \
               "(Id INTEGER PRIMARY KEY, Nombre VARCHAR(100), Apellido VARCHAR(100))")

alumnos = [(1, 'Leonel', 'Messi'),
           (2, 'Cristiano', 'Ronaldo'),
           (3, 'Neymar', 'Da Silva'),
           (4, 'Kylian', 'Mbappé'),
           (5, 'Karim', 'Benzema'),
           (6, 'Andres', 'Iniesta'),
           (7, 'Pedro', 'González'),
           (8, 'Carlos', 'Poyol'),
           (9, 'Hakim', 'Ziyech'),
           (10, 'Achraf', 'Hakimi')]

# Guardamos los cambios haciendo un commit
conexion.commit()

# Consultamos los asi existe el alumno por nombre
rows = cursor.execute('SELECT * FROM alumnos WHERE Nombre="Andres"')
for row in rows:
    print(row)


conexion.close()