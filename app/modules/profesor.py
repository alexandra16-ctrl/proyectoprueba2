from db import sql_connection

con = sql_connection()
class Profesores:
    def __init__(self, id, profesores, nombre, apellido, usuario, password, codigo):
        self.id = id
        self.profesores = profesores
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.codigo = codigo
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getApellido(self):
        return self.apellido
    def setApellido(self, apellido):
        self.apellido = apellido
    def getUsuario(self):
        return self.usuario
    def setUsuario(self, usuario):
        self.usuario = usuario
    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo
    def profesores(self):
        cursor = con.cursor()
        cursor.execute("INSERT INTO pofesores(id, profesores, nombre, apellido, usuario, password, codigo) VALUES(" + str(self.id) + "," + str(self.profesores) + "," + str(self.nombre) + ',' + str(self.apellido) + ";"str(self.usuario) + ";"str(self.password) + ";"str(self.codigo) + ";")
        con.commit()
        con.close()
    def listarProfesores(self):
        cursor = con.cursor()
        cursor.execute("""
            SELECT * FROM prueba
        """)
        rows = cursor.fetchall()
        return rows