import oracledb
from models import departamento

class ServiceDepartamentos:
    def __init__(self):
        self.connection=oracledb.connect(user="SYSTEM", password="oracle", dsn="localhost/FREEPDB1") 
        print("Estamos Conextados")
    def insertarDepartamentos(self, numero, nombre, localidad):
        cursor=self.connection.cursor()
        sql="insert into DEPT values (:numero, :nombre, :localidad)"
        cursor.execute(sql, (numero, nombre, localidad, ))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    def eliminarDepartamentos(self, id):
        cursor=self.connection.cursor()
        sql="delete from DEPT where DEPT_NO=:id"
        cursor.execute(sql, (id, ))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    def updateDepartamentos(self, numero, nombre, localidad):
        cursor=self.connection.cursor()
        sql="update DEPT set DNOMBRE=:nombre, LOC=:localidad where DEPT_NO=:numero"
        cursor.execute(sql, (nombre, localidad, numero, ))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
    def recogerDatosDepartamentos(self):
        cursor=self.connection.cursor()
        sql="select * from DEPT"
        cursor.execute(sql)
        listaDepartamento=[]
        for row in cursor:
            dept=departamento.Departamento()
            dept.idDepartamento=row[0]
            dept.nombre=row[1]
            dept.localidad=row[2]
            listaDepartamento.append(row)
        return listaDepartamento
    def getNombreDepartamento(self, iddepartamento):
        cursor=self.connection.cursor()
        sql="select  from DEPT where DEPT_NO=:iddepartamento"
        cursor.execute(sql, (iddepartamento, ))
        row=cursor.fetchone()
        dept=departamento.Departamento()
        dept.idDepartamento=row[0]
        dept.nombre=row[1]
        dept.localidad=row[2]
        return dept
      
