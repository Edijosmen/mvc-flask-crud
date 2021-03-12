
from src.config.db import mysql

class UsuarioModel():
    def listarUser(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('select * from persona')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    def crearUser(serlf,nombre,apellido,celular,correo,contrasena):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into persona(nombre,apellido,celular,correo,contrasena) values(%s,%s,%s,%s,%s)', (nombre,apellido, celular, correo, contrasena))
        cursor.close()
    def update(self,id,nombre,apellido,celular,correo,contrasena):
        cursor = mysql.get_db().cursor()
        cursor.execute('update persona set nombre = %s, apellido = %s, celular = %s,correo = %s, contrasena = %s WHERE idpersona=%s',(nombre,apellido, celular, correo, contrasena, id))
        

