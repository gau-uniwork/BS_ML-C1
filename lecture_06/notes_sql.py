# %% [markdown]
# # SQL

# %% [markdown]
# #### SQL SERVER

# %%
import pyodbc

# %%
conn_str = "Driver=SQL SERVER;Server={YOUR_SQLSERVER};Database={DATABASE};Trust_Coneection=yes;"

# %%
conn = pyodbc.connect(conn_str)

curr = conn.cursor()

curr.execute("SELECT * FROM Product WHERE id = ?", 1)
rows = curr.fetchall()
# curr.fetchone()
# curr.fetchmany(2)

for row in rows:
    print(row)

# %%
curr.execute("INSERT INTO Categories VALUES(?, ?)", ("cat1", "sdfsdf"))

curr.commit()

# %%
conn.close()

# %% [markdown]
# #### MYSQL

# %%
import mysql.connector

# %%
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

curr = db.cursor()
curr.execute("CREATE DATABASE estore")

# %%
curr.execute("SHOW DATABASES")
for d in curr:
    print(d)

# %%
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="estore"
)
curr = db.cursor()

curr.execute("CREATE TABLE Product (name VARCHAR(255), description VARCHAR(500), price DECIMAL(4, 2))")

# %%
curr.reset()

# %%
curr.execute("SHOW TABLES")
for t in curr:
    print(t)

# %%
curr.reset()

# %%
sql = "INSERT INTO Product (name, description, price) VALUES(%s, %s, %s)"
# val = ("GeForce RTX 4090", "awesome", 10)
val = [
    ("GeForce RTX 4090", "awesome", 10),
    ("Intel Core i9-12kf", "awesome", 10)
]

# curr.execute(sql, val)
curr.executemany(sql, val)
db.commit()
curr.rowcount

# %%
curr.reset()
curr.execute("SELECT * From Product")

products = curr.fetchall()

for p in products:
    print(p)
