import pyodbc

connection=pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=PAPATYA\SQLEXPRESS01;"
    "Database=master;"
    "Trusted_Connection=yes;",
    autocommit=True
)

cursor=connection.cursor()
print("SQL ile bağlantı kuruldu")

createDatabaseQuery="CREATE DATABASE LibraryDB"
cursor.execute(createDatabaseQuery)
connection.commit()
print("LibraryDB veritabanı oluşturuldu")

connection.close()
connection=pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=PAPATYA\SQLEXPRESS01;"
    "Database=LibraryDB;"
    "Trusted_connection=yes;"
)
cursor=connection.cursor()
print("Library veritabanına bağlanıldı.")

createTableQuery="""
CREATE TABLE Books(
    ID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100) NOT NULL,
    Author NVARCHAR(100) NOT NULL,
    Price DECIMAL(20,2) NOT NULL,
    Stock INT NOT NULL

)
"""
cursor.execute(createTableQuery)
connection.commit()
print("Books tablosu oluşturuldu")

insertQuery="INSERT INTO Books(Title,Author,Price,Stock) VALUES(?,?,?,?)"
cursor.execute(insertQuery, ("The Catcher in the Rye", "J.D. Salinger", 29.99, 15))
cursor.execute(insertQuery, ("To Kill a Mockingbird", "Harper Lee", 24.99, 10))
cursor.execute(insertQuery, ("1984", "George Orwell", 19.99, 20))
connection.commit()
print("Veriler eklendi.")

updateQuery = "UPDATE Books SET Stock=? WHERE Title=?"
cursor.execute(updateQuery, (25, "1984"))
connection.commit()
print("Veriler güncellendi.")


deleteQuery = "DELETE FROM Books WHERE Title=?"
cursor.execute(deleteQuery, ("The Catcher in the Rye",))
connection.commit()
print("Veri silindi.")


alterTableQuery = "ALTER TABLE Books ADD Genre NVARCHAR(50)"
cursor.execute(alterTableQuery)
connection.commit()
print("Tabloya 'Genre' sütunu eklendi.")

selectQuery = "SELECT * FROM Books WHERE Price < 20"
cursor.execute(selectQuery)
rows = cursor.fetchall()
print("Fiyatı 20 birimden düşük olan kitaplar:")
for row in rows:
    print(row)


dropTableQuery = "DROP TABLE Books"
cursor.execute(dropTableQuery)
connection.commit()
print("Books tablosu silindi.")
