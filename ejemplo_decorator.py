# def decorador(x):
#     def envelope():
#         print("Esto se añade")
#         x()
#     return envelope

# @decorador
# def saludo():
#     print("Hola")

# @decorador
# def adios():
#     print("Adios")

# saludo()
# adios()

def mayusculas(x):
    def envelope(texto):
        return x(texto).upper()
    return envelope

@mayusculas
def mensaje(nombre):
    return f"{nombre},recibiste un mensaje"

print(mensaje("Cesar"))