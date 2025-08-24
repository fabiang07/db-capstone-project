import mysql.connector as connector

# Configuración conexión, reemplaza usuario y contraseña por los correctos
connection = connector.connect(
    user="lemon_admin",
    password="GMTh2017*",
    host="localhost",  # o donde esté tu servidor MySQL
    database="littlelemondb"
)

# Crear cursor para ejecutar consultas
cursor = connection.cursor()


show_tables_query = "SHOW tables"
cursor.execute(show_tables_query)

# Obtener todos los resultados a la vez
results = cursor.fetchall()

# Imprimir los nombres de las tablas
print("Tablas en la base de datos:")
for table in results:
    print(table[0])


query = """
SELECT c.Name, c.Email, c.Phone, o.TotalCost
FROM orders o
JOIN bookings b ON o.BookingID = b.BookingID
JOIN customers c ON b.CustomerID = c.CustomerID
WHERE o.TotalCost > 60
"""

cursor.execute(query)

results = cursor.fetchall()

print("Clientes con pedidos mayores a $60:")
for (name, email, phone, totalcost) in results:
    print(f"Nombre: {name}, Email: {email}, Teléfono: {phone}, Total Pedido: ${totalcost}")


cursor.close()
connection.close()
