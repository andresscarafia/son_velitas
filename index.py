#! index.py

from tkinter import ttk
from tkinter import *
from tkinter.tix import NoteBook

class Main:
    def __init__(self, window):



        
        self.root = window
        self.root.title('Son Velitas - by Flor')

        tab_control = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Precios de los Productos')
        tab_control.add(tab2, text='Insumos de los Productos')
        tab_control.add(tab3, text='Tab 3')
        tab_control.grid()
        #Crear un contenedor de Frame 1 para los costos, precios y ganancias
        frame1 = LabelFrame(tab1, text= 'Precios de los Productos')
        frame1.grid(row=0, column=0, columnspan=5, pady= 20)

        #Columna 0: Productos
        Label(frame1, text='Producto').grid(row=1, column=0)

        Label(frame1, text='Vela bombe').grid(row=2, column=0)
        Label(frame1, text='Vela Whiskey').grid(row=3, column=0)
        Label(frame1, text='Vela cuenco 8').grid(row=4, column=0)
        Label(frame1, text='Vela cuenco 10').grid(row=5, column=0)
        Label(frame1, text='Vela cuenco 12').grid(row=6, column=0)
        Label(frame1, text='Vela caramelera').grid(row=7, column=0)
        Label(frame1, text='Difusor 100ml').grid(row=8, column=0)
        Label(frame1, text='Difusor 125ml').grid(row=9, column=0)
        Label(frame1, text='Difusor 250ml').grid(row=10, column=0)

        Button(frame1, text='Actualizar Precio', command=None).grid(row=2, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=3, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=4, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=5, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=6, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=7, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=8, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=9, column=4)
        Button(frame1, text='Actualizar Precio', command=None).grid(row=10, column=4)

        Label(frame1, text='Costo').grid(row=1, column=1)
        Label(frame1, text='Precio').grid(row=1, column=2)
        Label(frame1, text='Ganancia').grid(row=1, column=3)

        #Frame 2 Indica los insumos para cada producto
        frame2 = LabelFrame(tab2, text=('Insumos de los Productos'))
        frame2.grid(row=0, column=5, columnspan=6)
        
        #1ro productos
        Label(frame2, text='Producto').grid(row=1, column=5)

        Label(frame2, text='Vela bombe').grid(row=2, column=5, rowspan= 5)
        Label(frame2, text='Vela Whiskey').grid(row=7, column=5, rowspan= 5)
        Label(frame2, text='Vela cuenco 8').grid(row=12, column=5, rowspan= 5)
        Label(frame2, text='Vela cuenco 10').grid(row=17, column=5, rowspan= 5)
        Label(frame2, text='Vela cuenco 12').grid(row=22, column=5, rowspan= 5)
        Label(frame2, text='Vela caramelera').grid(row=27, column=5, rowspan= 5)
        Label(frame2, text='Difusor 100ml').grid(row=32, column=5, rowspan= 5)
        Label(frame2, text='Difusor 125ml').grid(row=37, column=5, rowspan= 5)
        Label(frame2, text='Difusor 250ml').grid(row=42, column=5, rowspan= 5)

        #2do Insumos
        Label(frame2, text='Insumo').grid(row=1, column=6)

        Label(frame2, text='Cera').grid(row=2, column=6)
        Label(frame2, text='Esencia').grid(row=3, column=6)
        Label(frame2, text='Pabilo').grid(row=4, column=6)
        Label(frame2, text='Ojal').grid(row=5, column=6)
        Label(frame2, text='Envase').grid(row=6, column=6)
        Label(frame2, text='Cera').grid(row=7, column=6)
        Label(frame2, text='Esencia').grid(row=8, column=6)
        Label(frame2, text='Pabilo').grid(row=9, column=6)
        Label(frame2, text='Ojal').grid(row=10, column=6)
        Label(frame2, text='Envase').grid(row=11, column=6)
        Label(frame2, text='Cera').grid(row=12, column=6)
        Label(frame2, text='Esencia').grid(row=13, column=6)
        Label(frame2, text='Pabilo').grid(row=14, column=6)
        Label(frame2, text='Ojal').grid(row=15, column=6)
        Label(frame2, text='Envase').grid(row=16, column=6)
        Label(frame2, text='Cera').grid(row=17, column=6)
        Label(frame2, text='Esencia').grid(row=18, column=6)
        Label(frame2, text='Pabilo').grid(row=19, column=6)
        Label(frame2, text='Ojal').grid(row=20, column=6)
        Label(frame2, text='Envase').grid(row=21, column=6)
        Label(frame2, text='Cera').grid(row=22, column=6)
        Label(frame2, text='Esencia').grid(row=23, column=6)
        Label(frame2, text='Pabilo').grid(row=24, column=6)
        Label(frame2, text='Ojal').grid(row=25, column=6)
        Label(frame2, text='Envase').grid(row=26, column=6)
        Label(frame2, text='Cera').grid(row=27, column=6)
        Label(frame2, text='Esencia').grid(row=28, column=6)
        Label(frame2, text='Pabilo').grid(row=29, column=6)
        Label(frame2, text='Ojal').grid(row=30, column=6)
        Label(frame2, text='Envase').grid(row=31, column=6)
        Label(frame2, text='Cera').grid(row=32, column=6)
        Label(frame2, text='Esencia').grid(row=33, column=6)
        Label(frame2, text='Pabilo').grid(row=34, column=6)
        Label(frame2, text='Ojal').grid(row=35, column=6)
        Label(frame2, text='Envase').grid(row=36, column=6)
        Label(frame2, text='Cera').grid(row=37, column=6)
        Label(frame2, text='Esencia').grid(row=38, column=6)
        Label(frame2, text='Pabilo').grid(row=39, column=6)
        Label(frame2, text='Ojal').grid(row=40, column=6)
        Label(frame2, text='Envase').grid(row=41, column=6)
        Label(frame2, text='Cera').grid(row=42, column=6)
        Label(frame2, text='Esencia').grid(row=43, column=6)
        Label(frame2, text='Pabilo').grid(row=44, column=6)
        Label(frame2, text='Ojal').grid(row=45, column=6)
        Label(frame2, text='Envase').grid(row=46, column=6)


        Label(frame2, text='Cantidad').grid(row=1, column=7)
        Label(frame2, text='Unidad').grid(row=1, column=8)
        Label(frame2, text='Precio x Unidad').grid(row=1, column=9)
        Label(frame2, text='Precio por uso').grid(row=1, column=10)

        #Frame 3 para los costos de los insumos
        frame3 = LabelFrame(tab3, text=('Costos de los Insumos'))
        frame3.grid(row=0, column=11, columnspan=5)
        Label(frame3, text='PLACEHOLDER').grid(row=1, column=11, columnspan=5)



        
        

        


        

if __name__ == '__main__':
    window = Tk()
    application = Main(window)
    window.mainloop()
