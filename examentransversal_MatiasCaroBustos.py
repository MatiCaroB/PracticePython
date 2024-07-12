import random,csv

trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
    

sueldosTrabajadores=[]
clasificaciontrabajadores=[]
total=0

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldoRandom=random.randint(300000,2500000)
        sueldosTrabajadores.append(sueldoRandom)
        
        
      
        
def estadísticas():
    print(f"sueldo más alto: {max(sueldosTrabajadores)}")
    print(f"sueldo más bajo: {min(sueldosTrabajadores)}")
   
    for sueldo in sueldosTrabajadores:
        total+=sueldo
        total=total/10

    print(f"El promedio de los sueldos es: ${total}")
    
    
def clasificacion():
    for trabajador in clasificaciontrabajadores:
        clasificaciontrabajadores.append(f"{trabajadores} su sueldo es: ${sueldosTrabajadores}")   


             
            

  
              
              
        


while True:
    print("1. Asignar sueldos aleatorios.")
    print("2. Clasificar sueldos.")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir.")
    try:
        op=(int(input("Ingrese con el correspondiente dígito que operación desea realizar: ")))
    except:
        print("Se debe ingresar un dígito desde el <1> hasta el <5>")
        
    
    match op:
        case 1:
            asignar_sueldos_aleatorios()
            print("Operación realizada")
            
        
        case 2:
            clasificacion()
           
        
        case 3:
            estadísticas()
        
        case 4:
            break
        
        case 5:
            print("Finalizando programa")
            print("Desarrollado por Matías Nicolás Caro Bustos")
            print("Rut 21.694.780-0")
            
            
            
        









































































































