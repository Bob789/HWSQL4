import sqlitelib

db_name: str = "sales.db"
conn, cursor = sqlitelib.connect_db(db_name)

product_name = input('enter new product name?')
product_price = float(input('enter new product name?'))

sqlitelib.update_query(
    cursor, conn,
    "INSERT INTO products (name, price) VALUES (?, ?)",
    (product_name, product_price))

result_select_products = sqlitelib.read_query(cursor, "SELECT * from products")
for item in result_select_products:
    print(item)

conn.close()
