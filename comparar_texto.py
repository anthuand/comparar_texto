#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import os
import time
from progress.bar import ChargingBar


def main():
    texto_original = open("original.txt","r")
    text_secundario = open("secundario.txt","r")
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

    barra= ChargingBar("Comparando:", max=100)
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

    pausa=input("Espero que te haya servido.")


if __name__ == "__main__":
    main()
