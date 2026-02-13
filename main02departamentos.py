from services import service02oracledepartamentos   
print("BEINVENIDOS A MI SERVICIO")
servicio=service02oracledepartamentos.ServiceDepartamentos()
print("Insertar departamento")
numero=int(input("ID del departamento: "))
nombre=input("Nombre del departamento: ")
localidad=input("Localidad: ")
registro=servicio.insertarDepartamentos(numero, nombre, localidad)
print("Elimina el")