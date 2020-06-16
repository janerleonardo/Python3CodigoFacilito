#!/usr/bin/env python 3.8
"""
Todos los metodos debe recibir self por conveccion, podria ser otra palabra pero se utiliza self
Existen 2 formas de  asignarle atributos a la clase, una es dentro de la clase y otra es directamente
en el objeto instanciado, la forma correcta utilizando el metodo __init__(selft) que corresponderia al contructor
"""
class Usuario:

    def __init__(self, nombre ='', apellido =''):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Saludados {0} {1}".format(self.nombre,self.apellido))
    #Se deficio el atributo en el objeto y en la clase se definnio un metodo para mustrarlo
    def mostrar_apodo(self):
        print(self.Apodo)
    #Para crear el atributo en  dentro de la clase se utilizan los metodos

usuario = Usuario("Janer", "Tegue")
#En el Objeto instanciado
usuario.Apodo = "Programador"
usuario.saludo()
usuario.mostrar_apodo()


