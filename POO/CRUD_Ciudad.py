import mysql.connector
from mysql.connector import Error


# Modelo: representa una fila de la tabla "CIUDAD"
class Ciudad:
    def __init__(self, codigo, nombre):
        self.codigo = codigo  # Clave de la ciudad (ej. 'TEC')
        self.nombre = nombre  # Nombre completo de la ciudad

    def __str__(self):
        return f"{self.codigo:<6} | {self.nombre:<15}"


# DAO: concentra todas las operaciones CRUD sobre la tabla "CIUDAD"
class CiudadDAO:
    def __init__(self, conexion):
        self._conexion = conexion
        # dictionary=True permite acceder a las columnas por nombre
        self._cursor = conexion.cursor(dictionary=True)

    # CREATE: agrega una ciudad nueva
    def insertar(self, ciudad):
        try:
            consulta = "INSERT INTO CIUDAD (codigo, nombre) VALUES (%s, %s)"
            self._cursor.execute(consulta, (ciudad.codigo, ciudad.nombre))
            self._conexion.commit()
            print(f"Ciudad registrada: {ciudad.codigo} - {ciudad.nombre}")
        except Error as error:
            # Si algo falla se deshacen los cambios pendientes
            self._conexion.rollback()
            print(f"No se pudo registrar '{ciudad.codigo}': {error}")

    # UPDATE: cambia el nombre de una ciudad existente
    def actualizar_nombre(self, codigo, nuevo_nombre):
        try:
            consulta = "UPDATE CIUDAD SET nombre = %s WHERE codigo = %s"
            self._cursor.execute(consulta, (nuevo_nombre, codigo))
            self._conexion.commit()
            # rowcount indica cuántas filas fueron afectadas
            if self._cursor.rowcount > 0:
                print(f"Ciudad '{codigo}' actualizada a: {nuevo_nombre}")
            else:
                print(f"No existe una ciudad con codigo '{codigo}'")
        except Error as error:
            self._conexion.rollback()
            print(f"No se pudo actualizar '{codigo}': {error}")

    # DELETE: borra una ciudad a partir de su código
    def eliminar(self, codigo):
        try:
            consulta = "DELETE FROM CIUDAD WHERE codigo = %s"
            self._cursor.execute(consulta, (codigo,))
            self._conexion.commit()
            if self._cursor.rowcount > 0:
                print(f"Ciudad '{codigo}' eliminada")
            else:
                print(f"No existe una ciudad con codigo '{codigo}'")
        except Error as error:
            self._conexion.rollback()
            print(f"No se pudo eliminar '{codigo}': {error}")

    # READ: devuelve todas las ciudades como objetos Ciudad
    def mostrar_todos(self):
        self._cursor.execute("SELECT codigo, nombre FROM CIUDAD ORDER BY codigo")
        filas = self._cursor.fetchall()
        return [Ciudad(fila['codigo'], fila['nombre']) for fila in filas]

    # Libera el cursor cuando ya no se necesita
    def cerrar_cursor(self):
        self._cursor.close()


# Clase más importante, administra el enlace con MySQL,
# sin ella ninguna otra clase podría trabajar con la base de datos
class Conexion:
    def __init__(self, host, usuario, contrasena, base_datos, puerto=3306):
        # Parámetros de conexión agrupados en un diccionario
        self._datos = dict(host=host, port=puerto, user=usuario,
                           password=contrasena, database=base_datos,
                           charset='utf8mb4')
        self._conexion = None

    # Abre la conexión; devuelve None si ocurre un error
    def conectar(self):
        try:
            self._conexion = mysql.connector.connect(**self._datos)
            if self._conexion.is_connected():
                print(f"Conexion establecida con la base de datos '{self._datos['database']}'")
            return self._conexion
        except Error as error:
            print(f"Error al conectar con la base de datos: {error}")
            return None

    # Cierra la conexión solo si sigue activa
    def cerrar(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()
            print("Conexion cerrada correctamente")


# Muestra una lista de ciudades en forma de tabla
def imprimir_ciudades(titulo, ciudades):
    print(f"\n----- {titulo} -----")
    print(f"{'Codigo':<6} | {'Nombre':<15}")
    print("-" * 24)
    for ciudad in ciudades:
        print(ciudad)
    print()


# Programa principal: ejecuta el flujo completo del CRUD
def main():
    bd = Conexion('localhost', 'root', '', 'almacen3a')
    conexion = bd.conectar()
    # Si no hubo conexión no tiene sentido continuar
    if conexion is None:
        return
    dao = CiudadDAO(conexion)

    # Estado inicial de la tabla
    imprimir_ciudades("CIUDADES ANTES DEL CRUD", dao.mostrar_todos())

    # Paso 1: insertar dos registros distintos
    print("== INSERTAR ==")
    dao.insertar(Ciudad('TEC', 'Tecate'))
    dao.insertar(Ciudad('SQN', 'San Quintin'))

    # Paso 2: modificar uno de los registros recién insertados
    print("\n== ACTUALIZAR ==")
    dao.actualizar_nombre('TEC', 'Tecate BC')

    # Paso 3: borrar uno de los registros
    print("\n== ELIMINAR ==")
    dao.eliminar('SQN')

    # Paso 4: mostrar cómo quedó la tabla
    imprimir_ciudades("CIUDADES DESPUES DEL CRUD", dao.mostrar_todos())

    # Cierre ordenado de recursos
    dao.cerrar_cursor()
    bd.cerrar()


main()