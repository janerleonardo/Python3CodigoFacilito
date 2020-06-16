def saluda():
    print("Hola mundo")

def crear_mensaje(nombre):
    mensaje ="Hola como estas {0}".format(nombre)
    return mensaje

print(crear_mensaje("Janer"))

def suma(val1,val2,val3):
    return val1 + val2 + val3

print(suma(10,20,30,))

def obtener_curso():
    return "Curso de Python", "Profesional?",3.6

curso, nivel, version = obtener_curso()
print(curso,nivel,version)

def crear_usuarios(nombre='',apellido='',edad=0):
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'nombre_completo': "{0} {1}".format(nombre,apellido),
        'edad' : edad
    }

usuario = crear_usuarios("Janer","Hijo de DIOS",32)
print(usuario["nombre"])
print(usuario["nombre_completo"])
print(usuario["apellido"])
print(usuario["edad"])

usuario = crear_usuarios(nombre="Janer",edad=32)
print(usuario["nombre"])
print(usuario["nombre_completo"])
print(usuario["apellido"])
print(usuario["edad"])
