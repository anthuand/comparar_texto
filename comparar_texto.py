#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    texto_1 = open("1.txt", "r")
    texto_2 = open("2.txt", "r")
    diferencias = []  # recibe una tupla ("palabra","texto.linea") donde indica la palabra que no concuerda y el texto y la linea en l formato "texto.linea"

    cantidad_lineas_1 = texto_1.readlines().__len__()
    cantidad_lineas_2 = texto_2.readlines().__len__()

    for linea_2 in texto_2.readlines():
        print(linea_2)


if __name__ == "__main__":
    main()
