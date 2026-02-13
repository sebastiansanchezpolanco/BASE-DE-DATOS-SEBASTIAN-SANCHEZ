from services import service01prueba
print("hello GitHub, soy un main")
texto=service01prueba.getSaludo()
pez=service01prueba.getMascota1()
leona=service01prueba.getMascota2()
print(f"Nombre: {pez.nombre} , Raza: {pez.raza}")
print(f"Nombre: {leona.nombre} , Raza: {leona.raza}")
print(texto)
lista =service01prueba.getListaMascotas()
for dato in lista:
    print(dato.nombre)
