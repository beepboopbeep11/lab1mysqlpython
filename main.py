import mysql.connector
from mysql.connector import Error

def test_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="kardashevskaia", 
            user="root",              
            password="kit2025"
        )
        
        if connection.is_connected():
            print("Успешно! Подключение к базе данных kardashevskaia установлено.")
            
            cursor = connection.cursor()
            cursor.execute("SELECT product_id, name, price FROM products;")
            products = cursor.fetchall()
            
            print("\n--- Список товаров из БД ---")
            for prod in products:
                print(f"ID: {prod[0]} | Товар: {prod[1]} | Цена: {prod[2]}$")
            print("----------------------------")
            
            cursor.close()
            connection.close()
            print("\nСоединение с БД закрыто.")

    except Error as e:
        print(f"Ошибка при работе с MySQL: {e}")

if __name__ == "__main__":
    test_db_connection()