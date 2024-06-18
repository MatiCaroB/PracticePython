
matriztrabajadores=["Nombre","Cargo","Sueldo Bruto","Descuento de Salud","Descuento de Afp","Sueldo líquido"]
def crear_trabajador():
    nombre=input("ingrese el nombre del trabajador: ")
    cargo=input("ingrese el cargo: ")
    sueldobruto=int(input("ingrese el sueldo bruto: "))
    
    descuentosalud= sueldobruto * 0.07
    descuentoafp=sueldobruto * 0.12

    sueldoliquido= sueldobruto-descuentosalud-descuentoafp
    trabajador=[nombre,cargo,sueldobruto,descuentosalud,descuentoafp,sueldoliquido]
    

 
    return trabajador


    



def imprimir_planillas(matriztrabajadores): 
    
        with open('archivo.txt','w') as archivo:
                archivo.write(str(matriztrabajadores))
                
           

def lista_trabajadores(matriztrabajadores):
    
    for datos in matriztrabajadores:
        print(datos)






opcionmenuprincipal=5
while opcionmenuprincipal!=4:
    print("1.-registrar trabajador")
    print("2.-listar trabajadores")
    print("3,-imprimir planillas de sueldos")
    print("4.-salir")

    opcionmenuprincipal=int(input("ingrese opcion(numero) >"))
    match opcionmenuprincipal:
        case 1:
            trabajador=crear_trabajador()
            matriztrabajadores.append(trabajador)
         
        case 2:
            lista_trabajadores(matriztrabajadores)
            
        case 3:
            imprimir_planillas(matriztrabajadores)
            
        case 4:
            print("gracias por usar nuestro sistema. adios")