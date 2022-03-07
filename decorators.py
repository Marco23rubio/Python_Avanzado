from datetime import datetime

def decorador(funcion_parametro):
    def wraper(*args,**kwargs):
        inicial_time = datetime.now()
        funcion_parametro(*args,**kwargs)
        final_time = datetime.now()
        total_time = final_time - inicial_time
        print("El tiempo de carga fue de: " + str(total_time.total_seconds())+" segundos")
    return wraper

@decorador 
def suma(a:int,b:int) ->int :
    return a+b

suma(5,5)