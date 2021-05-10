#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import os
import time
from progress.bar import ChargingBar
from tkinter import *
from tkinter import ttk,scrolledtext


# ############################################--------->Interfaz Grafica<--------########################################
class Aplicacion():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry('1000x600')
        self.main_window.title('Ads-aplicacion')
        self.main_window.configure(bg='burlywood')
        self.area_texto=scrolledtext.ScrolledText(self.main_window, width=100, height=30).pack(side=TOP)
        self.bcomparar = ttk.Button(self.main_window, text='Comparar', command=comparar(self)).pack(side=LEFT)
        self.bsalir = ttk.Button(self.main_window, text='Salir', command=self.main_window.destroy()).pack(side=RIGHT)
        self.bcomparar.focus_set()
        self.main_window.mainloop()


def comparar(self):
    texto_original = open("original.txt", "r")
    text_secundario = open("secundario.txt", "r")
    os.system("cls")

    print("""			  
                               ( ( (                   
                                ) ) )                 
                               ( ( (          
                             '. ___ .'       
                            '  (> <) '        
                    --------ooO-(_)-Ooo----------
                    Gracias por usar mis servicios
                    
                             ② ⓪ ② ⓪
                               ⌜   ⌝
                                ads
                               ⌞   ⌟
    """)

    print("Vamos a comparar...")

    barra = ChargingBar("Comparando:", max=100)
    for num in range(100):
        time.sleep(0.05)
        barra.next()
    barra.finish()
    time.sleep(1)

    lineas1 = texto_original.readlines()
    lineas2 = text_secundario.readlines()
    diferencia = difflib.Differ()
    generador_diferencia = diferencia.compare(lineas2, lineas1)

    print("\n".join(generador_diferencia))

    self.area_texto.insert(INSERT, 'aqgjghjdssdgdfgdgthgfbdvcbcvghjjgjg')
    pausa = input("Espero que te haya servido.")



def main():
    myApp = Aplicacion()
    return 0


if __name__ == "__main__":
    main()
