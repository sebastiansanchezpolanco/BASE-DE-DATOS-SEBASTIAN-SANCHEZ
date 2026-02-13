import oracledb

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
        sql="delete from DEPT where DEPT_NO:id"
        cursor.execute(sql, (id, ))
        self.connection.commit()
        registros=cursor.rowcount
        cursor.close()
        return registros
