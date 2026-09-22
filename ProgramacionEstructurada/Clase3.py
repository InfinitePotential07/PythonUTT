#1.- Control de acceso por edad
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Acceso concedido: Eres mayor de edad.")
else:
    print("Acceso denegado: Eres menor de edad.")

#2.- Validacion de contraseñas
validacion = "admin123"
password = "user123"

if password == validacion:
    print("¡Inicio de sesión exitoso!")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo.")

#3.- Verificación de stock en tienda
stock = 0

if stock > 0:
    print("Producto disponible para compra.")
else:
    print("Lo sentimos, este producto está agotado.")
#4.- Estado de una conexión
conectado = False

if conectado:
    print("Descargando actualización...")
else:
    print("Error: No hay conexión a internet.")

# 5.- Sistema de calificaciones escolares
nota = 85

if nota >= 90:
    print("Calificación: A (Excelente)")
elif nota >= 80:
    print("Calificación: B (Muy Bueno)")
elif nota >= 70:
    print("Calificación: C (Suficiente)")
else:
    print("Calificación: F (Reprobado)")

#6.- Categorización por rangos de edad
edad = 25

if edad < 12:
    print("Categoría: Niño")
elif edad < 18:
    print("Categoría: Adolescente")
elif edad < 65:
    print("Categoría: Adulto")
else:
    print("Categoría: Adulto Mayor")

#7.- Calcular el costo de envío según el peso
pesoPaquete = 7.5  # en kg

if pesoPaquete <= 2:
    costo = 5.0
elif pesoPaquete <= 5:
    costo = 10.0
elif pesoPaquete <= 10:
    costo = 20.0
else:
    costo = 35.0

print(f"El costo de envío es de ${costo}")

#8.- Semáforo inteligente
colorSemaforo = "amarillo"

if colorSemaforo == "verde":
    print("Avanzar")
elif colorSemaforo == "amarillo":
    print("Frenar con precaución")
elif colorSemaforo == "rojo":
    print("Detenerse por completo")
else:
    print("Semáforo intermitente / Descompuesto")

#9.- Menú de opciones (Comandos de consola)
comando = "guardar"

match comando:
    case "crear":
        print("Creando nuevo archivo...")
    case "guardar":
        print("Guardando cambios en el disco...")
    case "eliminar":
        print("Eliminando archivo...")
    case _:
        print("Comando no reconocido.")

#10.- Códigos de respuesta HTTP
codigoEstado = 404

match codigoEstado:
    case 200 | 201:  # El operador '|' sirve como un "o"
        print("Conexión exitosa.")
    case 400:
        print("Petición incorrecta (Bad Request).")
    case 404:
        print("Recurso no encontrado (Not Found).")
    case 500:
        print("Error interno del servidor.")
    case _:
        print("Código de estado desconocido.")
#11.- Desempaquetado de Tuplas
# El dato representa un punto en un plano: (x, y)
punto = (0, 5)

match punto:
    case (0, 0):
        print("El punto está en el origen exacto.")
    case (x, 0):
        print(f"El punto está sobre el eje X en la posición {x}.")
    case (0, y):
        print(f"El punto está sobre el eje Y en la posición {y}.")
    case (x, y):
        print(f"El punto está en las coordenadas ({x}, {y}).")

#12.- Identificar tipos de archivos por extensión

archivo = "foto.png"
extension = archivo.split(".")[-1]
match extension:
    case "jpg" | "jpeg" | "png":
        print("Tipo de archivo: Imagen")
    case "mp4" | "mkv" | "avi":
        print("Tipo de archivo: Video")
    case "pdf" | "docx" | "txt":
        print("Tipo de archivo: Documento de texto")
    case _:
        print("Extensión de archivo no soportada.")
