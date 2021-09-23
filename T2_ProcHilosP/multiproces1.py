import multiprocessing as mp
from multiprocessing.context import Process
from multiprocessing.queues import Queue
import time

# nCPU=mp.cpu_count()
# print(nCPU)
# print(mp.current_process())

## ejemplo 1
def tUNO():
    print(f"Proceso hijo con pID: {mp.current_process().pid}")
    time.sleep(3)
    print("Fin processo hijo")
    
def main1():
    print(f"Proceso padre don pID: {mp.current_process().pid}")
    p1 = mp.Process(target=tUNO)
    p1.start()
    p1.join()
    print("Fin proceso padre")
 
## ejemplo 2  
def tDOS():
    print(f"proceso con nombre: {mp.current_process().name}")
    
def main2():
    p2 = mp.Process(target=tDOS,name="Proceso num 2")
    p2.start()
    p2.join()
    
## ejemplo 3
def tTRES():
    pActual=mp.current_process()
    print(f"proceso hijo pid: {pActual.pid}")
    for i in range(10):
        print(f"PH salida: {i}")
        time.sleep(1)
    
def main3():
    p3 = mp.Process(target=tTRES)
    p3.start()
    print("Proceso Padre ha terminado, termina el main.")
    print("Proceso hijo terminando...")
    print("Proceso hijo terminado")
    time.sleep(6)
    p3.terminate()
    
## ejemplo 4
def tCUATRO(num, q):
    print(f"Se pone en la cola {num}*{num}")
    q.put(num*num)

def main4():
    my_queue = mp.Queue()
    p4 = mp.Process(target=tCUATRO, args=(5,my_queue))
    p4.start()
    p4.join()
    print(f"Se lee de la cola: {my_queue.get()}")
    


if __name__=='__main__':   
    #main1() #ej1
    #main2() #ej2
    #main3() #ej3
    main4() #ej4