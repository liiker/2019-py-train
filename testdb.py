import mysql.connector

conn = mysql.connector.connect(
    user='homestead', password='secret',
    database='homestead',
    use_unicode=True, port=33060)

if not conn.is_connected():
    print("connected failed")


def query(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows


cars = query(conn, 'select * from cars limit 1')
parks = query(conn, 'select * from parks limit 1')

conn.close()

print(cars)
print(parks)
