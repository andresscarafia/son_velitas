#
'''
Aca voy a desarrollar el GUI de la app para escritorio
'''

from tkinter import ttk
from tkinter import *


root = Tk()
root.title('Son Velitas - by Flor')
root.geometry('500x500')

bg_img = PhotoImage(file= r'C:\Users\andre\Pc VIeja\Programacion\Proyectos\son_velitas\logo.png')
bg_label = Label(root, image= bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def actualizar_precio():
    new_window = Toplevel(root)
    new_window.title('Actualizar Precio')
    new_window.geometry('220x50')
    new_window.grab_set()
    Label(new_window, text='Nuevo Precio:', padx=10).grid(row=1, column=0)
    entry = Entry(new_window, justify=RIGHT, width=8)
    entry.grid(row=1, column=1)
    nuevo_precio = entry.get()
    b1=Button(new_window, text='Actualizar', command=lambda:[precio(nuevo_precio), new_window.destroy()])
    b1.grid(row=1, column=2)
    #new_window.grab_release()

def precio(p2):
    precio1.configure(text = p2)
    #new_window.destroy()


#Etiquetas
Label(root, text='Precio', bg='#A3DBE0').grid(row=0, column=1)
Label(root, text='Vela Bombé', bg='#A3DBE0').grid(row=1, column=0)
precio1=Label(root, text='0', bg='#A3DBE0')
precio1.grid(row=1, column=1)
Label(root, text='Vela Whiskey', bg='#A3DBE0').grid(row=2, column = 0)
Label(root, text='Vela chica', bg='#A3DBE0').grid(row=3, column = 0)
Label(root, text='Vela Caramelera', bg='#A3DBE0').grid(row=4, column = 0)
Label(root, text='Vela Cuenco 10', bg='#A3DBE0').grid(row=5, column = 0)
Label(root, text='Vela Cuenco 12', bg='#A3DBE0').grid(row=6, column = 0)
print(precio1.cget('text'))
Button(root, text='Actualizar Precio', command=actualizar_precio).grid(row=1, column=3)
print(precio1.cget('text'))


#Sin esto no anda:
root.mainloop()