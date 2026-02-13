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
    leona=mascotas.Mascota()
    leona.nombre="Nala"
    leona.raza="Leon"
    leona.edad=18
    listaMascotas.append(leona)
    leon=mascotas.Mascota()
    leon.nombre="Simba"
    leon.raza="Leon"
    leon.edad=18
    listaMascotas.append(leon)
    return listaMascotas
