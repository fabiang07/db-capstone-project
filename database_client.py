import mysql.connector as connector
import mysql.connector as connector
from mysql.connector import Error

def create_connection():
    """Crear conexión a la base de datos Little Lemon"""
    try:
        connection = connector.connect(
            host='localhost',
            database='littlelemondb',
            user='lemon_admin',  # Usuario que creaste anteriormente
            password='GMTh2017*'  # Reemplaza con tu contraseña
        )
        
        if connection.is_connected():
            print("¡Conexión exitosa a Little Lemon DB!")
            return connection
            
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Probar la conexión
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tablas en la base de datos:")
        for table in tables:
            print(f"- {table[0]}")
        
        cursor.close()
        conn.close()
        print("Conexión cerrada correctamente.")
