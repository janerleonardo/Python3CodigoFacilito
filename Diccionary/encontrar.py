diccionario = {"a": 1,"b": 2,"c": 3,"a": 4}

resultado = "z" in diccionario

print(resultado)
##Metodo Get
resultado1 = diccionario.get("z","La llave no existe") # la mas recomendada

print(resultado1)
"""
SetDefault si ingresas un llave  existente te retorna el valor, si no existe crea la llave con el valor 
por defecto  en el srgundo parametro 
"""
resultado2 = diccionario.setdefault("z", 32)
print(resultado2)
print(diccionario)
