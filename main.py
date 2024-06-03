import mysql.connector


mydb = mysql.connector.connect(
host="bix0jdccffmo9ahbcp8w-mysql.services.clever-cloud.com",
user="ugswo07jvztzihie",
password="pJw8mMBBd8uU5AM5b8ZY",
database="bix0jdccffmo9ahbcp8w"
)
# Crear un cursor
mycursor = mydb.cursor()
# Ejecutar consulta
mycursor.execute("SELECT * FROM Productos")
# Obtener resultados
resultados = mycursor.fetchall()
# Iterar sobre los resultados
for fila in resultados:
  print(fila)
# Cerrar conexión
mydb.close()