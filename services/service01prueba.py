from models import mascotas
def getSaludo():
    return "hoy es juernes"
def getMascota1():
    dato=mascotas.Mascota()
    dato.nombre="Flounder"
    dato.raza="Pez"
    dato.edad=22
    return dato
def getMascota2():
    dato=mascotas.Mascota()
    dato.nombre="Nala"
    dato.raza="Leon"
    dato.edad=18
    return dato
def getListaMascotas():
    listaMascotas=[]
    dato=mascotas.Mascota()
    dato.nombre="Nala"
    dato.raza="Leon"
    dato.edad=18
    listaMascotas.append(leona)
    dato=mascotas.Mascota()
    dato.nombre="Simba"
    dato.raza="Leon"
    dato.edad=18
    listaMascotas.append(leon)

