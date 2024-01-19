# Leandro Mieres

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Coutas"
)

cursor = conexion.cursor()

sqlsoc = "CREATE TABLE socios \
        (numsocio INT AUTO_INCREMENT PRIMARY KEY,\
        nombre VARCHAR(50),\
        apellido varchar(50),\
        dni int,\
        fechanacimiento date,\
        domicilio varchar(50),\
        telefono int,\
        categoria int)"

sqlcat = "CREATE TABLE categoria \
        (idcategoria INT AUTO_INCREMENT PRIMARY KEY,\
        categoria VARCHAR(50),\
        importe_categoria int)"

sqlcuo = "CREATE TABLE cuotas \
        (numsocio INT AUTO_INCREMENT ,\
        mes date ,\
        año date ,\
        importe int,\
        CONSTRAINT PK_cuotas PRIMARY KEY (numsocio, mes, año))"

sqlcob = "CREATE TABLE cobros \
        (numsocio INT AUTO_INCREMENT,\
        mes date ,\
        año date ,\
        fechacobro date,\
        importe int,\
        CONSTRAINT PK_cobros PRIMARY KEY (numsocio, mes, año))"

    # Ejecutar las consultas SQL
cursor.execute(sqlsoc)
cursor.execute(sqlcat)
cursor.execute(sqlcuo)
cursor.execute(sqlcob)

conexion.commit()