import multiprocessing as mp

def pUNO(pidPadre):
    print(f"PID padre: {pidPadre}")
    print(f"Proceso hijo con pID: {mp.current_process().pid}")
    print(f"proceso con nombre: {mp.current_process().name}")
    print("Fin processo hijo")
    
def main():
    nombres =["Proceso 1", "proceso dos", "P3"]
    procesos = []
    
    for i in range(len(nombres)):
        procesos.append(mp.Process(target=pUNO,
                                   name=nombres[i], 
                                   args=(mp.current_process().pid,)))
        
    for i in range(len(procesos)):
        procesos[i].start()
        
    for i in range(len(procesos)):
        procesos[i].join()
    
if __name__=='__main__':   
    main()
