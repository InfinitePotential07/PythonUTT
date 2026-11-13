import mysql.connector

def conectar_y_consultar(config, consulta_sql):

    try:
        # Estrablecer conexion
        conexion = mysql.connector.connect(**config)
        print("Conexion exitosa")
        # Crear cursor con resultados como diccionario
        cursor = conexion.cursor(dictionary = True)
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        # Cerrar recursos
        cursor.close()
        conexion.close()
        return resultados
    except mysql.connector.Error as error:
        print(f"Error de conexion o consulta: {error}") 

# Prueba de ejecucion
def main():
    configuracion = {
        "host" : "localhost",
        "port" : 3306,
        "user" : "root",
        "password" : "",
        "database" : "almacen3a",
        "charset" : "utf8mb4",
        "connect_timeout" : 10 
    }


    consulta = "SELECT * FROM PRODUCTO"
    resultados = conectar_y_consultar(configuracion, consulta)
    print("\n                            ------Listados de productos---------")
    print(f"{"Codigo" :<10} | {"Nombre" :<22} | {"Descripcion" :<50} | {"Precio":<8}")
    for row in resultados:
        print(f"| {row["codigo"]:<10} | {row["nombre"]:<20} | {row["descripcion"]:<50} | {row["precio"]:<8}")
main()