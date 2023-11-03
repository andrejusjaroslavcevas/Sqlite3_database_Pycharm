import sqlite3

conn = sqlite3.connect("candies_database.db")
c = conn.cursor()

with conn:
    c.execute("CREATE TABLE IF NOT EXISTS candy (name text, type text, price integer, quantity integer)")

enter_data = 'yes'

while enter_data == 'yes':
    print('Enter candy details:')
    name = input('The name of candy: ')
    type = input('The type of candy: ')
    price = float(input('The price of candy (kg): '))
    quantity = int(input('The quantity of candy (unit): '))
    enter_data = input('Do you still want to enter data? (yes/no): ')
    with conn:
        c.execute(f"INSERT INTO candy VALUES ('{name}', '{type}', {price}, {quantity})")

with conn:
    c.execute("SELECT * FROM candy")
    print(c.fetchall())

