
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("Se realizará un cálculo: ")
        funcion_parametro(*args)
        print("A finalizado el cálculo: ")
    return funcion_interior

@funcion_decoradora
def suma(x,y):
    print(x+y)

suma(10,5)

