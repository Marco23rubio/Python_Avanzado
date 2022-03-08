import time

# def fibo_gen(maxi:int) ->int:
#     n1=0
#     n2=1 
#     count=0
#     suma=0
#     while True:
#         if count == 0:
#             count += 1
#             yield n1
#         elif count == 1:
#             count += 1
#             yield n2
#         else:
#             suma = n1+n2
#             if suma >= maxi:
#                 raise StopIteration
#             n1 , n2 = n2 , suma 
#             yield suma


# fibonacci = fibo_gen(555)
# for element in fibonacci:
#     print(element)
#     time.sleep(0.5)

def fibo_dos(maxi:int) -> int:
    a , b = 0 , 1
    while a <= maxi:
        yield a
        a , b = b , b+a  

if __name__ == "__main__":
    algo = input("Dame un máximo: ")
    assert type(algo) == int , "Solo puedes poner numeros"
    assert algo > 0 , "Solo puedes poner numeros positivos"
    algo = int(algo)
    fibonacci = fibo_dos(algo)
    for element in fibonacci:
        print(element)
        time.sleep(0.2)