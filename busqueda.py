mensaje = "Este es un texto un poco grande en cuanto a logitud de caracteres se refiere"
print(mensaje.count("texto"))
print("texto" in mensaje)
print("texto" not in mensaje)
print(mensaje.find("texto")) # Saca el indice donde esta el texto
resultado = mensaje.find("texto")
resultado = mensaje[resultado: resultado + len("texto")]
print(resultado)
print(mensaje.startswith("E"))
print(mensaje.startswith("e"))
print(mensaje.endswith("E"))
print(mensaje.endswith("e"))
