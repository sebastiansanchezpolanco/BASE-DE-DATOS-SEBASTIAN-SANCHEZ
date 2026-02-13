from services import service02oracledepartamentos   
print("BEINVENIDOS A MI SERVICIO")
print("Que quieres hacer?")
print("1. Insertar") 
print("2. Eliminar")
print("3. Modificar")
print("4. Visualizar departamento")
opcion=int(input("Selecciona una opcion"))
if(opcion==1):
    servicio=service02oracledepartamentos.ServiceDepartamentos()
    print("Insertar departamento")
    numero=int(input("ID del departamento: "))
    nombre=input("Nombre del departamento: ")
    localidad=input("Localidad: ")
    registro=servicio.insertarDepartamentos(numero, nombre, localidad)
elif(opcion==2):
    servicio=service02oracledepartamentos.ServiceDepartamentos()
    print("Elimina un departamento")
    dept_no=int(input("Inserta el departamento a eliminar "))
    registro=servicio.eliminarDepartamentos(dept_no)
elif(opcion==3):
    servicio=service02oracledepartamentos.ServiceDepartamentos()
    print("Modificar departamento")
    numero=int(input("ID del departamento a modificar: "))
    nombre=input("Nombre del departamento a modificar: ")
    localidad=input("Localidad a modifica: ")
    registro=servicio.updateDepartamentos(numero, nombre, localidad)
elif(opcion==4):
    servicio=service02oracledepartamentos.ServiceDepartamentos()
    departamento=int(input("Visualizar el departamento "))
    registro=servicio.getNombreDepartamento(departamento)
    print(f"nombre: {registro[0]}, localidad: {registro[1]}")
else:
    print("Opcion no valida")
servicio=service02oracledepartamentos.ServiceDepartamentos()
listadepartamentos=servicio.recogerDatosDepartamentos()
for i in listadepartamentos:
    print(f"numero:{i[0]}, nombre: {i[1]}, localidad: {i[2]} ")