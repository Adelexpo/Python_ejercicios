import tkinter
from tkinter import *
from tkinter import messagebox as MessageBox

root = tkinter.Tk()

frame = Frame(root)
frame.pack()

frame.config(bg='Grey')
frame.config(width=480, height=520)

def reset():
    opcion.set(None)

# lable titulo
label1 = Label(frame, text=" LENGUAGES DE PROGRAMACIÓN", bg="Green")
label1.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# label datos personales
label1 = Label(frame, text=" Datos personales:", bg="Grey")
label1.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# Campo de datos personales
entry2 = Entry(frame)
entry2.grid(column=1, row=2, sticky=tkinter.W, padx=5, pady=5)
label2 = Label(frame, text="Nombre y Apellidos")
label2.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)

entry3 = Entry(frame)
entry3.grid(column=1, row=3, sticky=tkinter.W, padx=5, pady=5)
label3 = Label(frame, text="Email")
label3.grid(column=0, row=3, sticky=tkinter.W, padx=5, pady=5)

entry4 = Entry(frame)
entry4.grid(column=1, row=4, sticky=tkinter.W, padx=5, pady=5)
label4 = Label(frame, text="Teléfono")
label4.grid(column=0, row=4, sticky=tkinter.W, padx=5, pady=5)

# campo seleccionar
# label texto
label5 = Label(frame, text=" Selecionar tu curso:", bg="Grey")
label5.grid(column=0, row=5, sticky=tkinter.W, padx=5, pady=5)







# Configuración de la raíz


opcion = tkinter.IntVar()
r1 = tkinter.Radiobutton(root, text="Python", variable=opcion,
                         value=1).pack()
r2 = tkinter.Radiobutton(root, text="Java", variable=opcion,
                         value=2).pack()
r3 = tkinter.Radiobutton(root, text="PHP", variable=opcion,
                         value=3).pack()
r4 = tkinter.Radiobutton(root, text="C#", variable=opcion,
                         value=4).pack()
r5 = tkinter.Radiobutton(root, text="ReactJS", variable=opcion,
                         value=5).pack()




def test():
    MessageBox.showinfo("Formulario ha sido enviado") # título, mensaje

Button(root, text = "Enviar", command=test).pack()


Button(root, text="Reset", command=reset, bg="Grey").pack()

root.mainloop()
