#Represa Hidroituango

#Entradas 
nivelAgua = float(input("Digite el nivel del agua: "))

#procesos 
if nivelAgua >= 0  and nivelAgua<=250:
    print(f"El sensor marca {nivelAgua}, muy bajo..")
elif nivelAgua>250 and nivelAgua<=400:
    print(f"El sensor marca {nivelAgua},operando normalmente..")
else:
    print(f"El sensor marca {nivelAgua}, PELIGRO")




#buscar listado con las fechas 

