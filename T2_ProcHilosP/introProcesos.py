# Multiprocessing 

import multiprocessing as mp
import time

def tarea(cadena):
    print(f"Hola {cadena}")

def calc_cuad(nums):
    print("Calcula el cuadrado de los numeros")
    for n in nums:
        print(f"El cuadrado de {n} es {n**2}")

def cubo(nums):
    print("Calcula los cubos de los numeros")
    for n in nums:
        print(f"El cubo de {n} es {n**3}")


if __name__=='__main__':

    # Ejemplo 1

    ts=time.time()

    p = mp.Process(target=tarea, args=('Lucas C.',))
    p.start()
    p.join()

    #Ejemplo 2

    nums=range(10)
    p1 = mp.Process(target=calc_cuad, args=(nums,))
    p1.start()
    p1.join()

    # Ejemplo 3

    p2=mp.Process(target=cubo,args=(nums,))
    p2.start()
    p2.join()

    print("FIN EJEMPLO")
    print(f"Tiempo secuencial: {time.time()-ts}")

    print("En realidad debe de quedar: ")

    tc=time.time()
    p = mp.Process(target=tarea, args=('Lucas C.',))
    p1 = mp.Process(target=calc_cuad, args=(nums,))
    p2=mp.Process(target=cubo,args=(nums,))

    p.start()
    p1.start()
    p2.start()

    p.join()
    p1.join()
    p2.join()

    print("FIN")
    print(f"Tiempo concurrente: {time.time()-tc}")
