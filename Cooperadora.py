##################
# Leandro Mieres #
##################

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", #cambiar a " " sin contraseña
    port='3306  ', #generalmete es el puerto 3306
    database="Coutas") #Depende de tu BD

cursor = conexion.cursor()
print("===================")
print("### Bienvenidos ###")
print("===================")
name=input("Por Favor, Ingrese Su Nombre: ")
print("===================================\n")

def select():
        print("===================================")
        print((name)+", "+"has Seleccionado MOSTRAR DATOS")
        print("===================================\n")

        print("============================")
        print((name)+", "+"Debera Ingresar Un DNI")
        print("============================\n")

        print("===================")
        a=int(input("Ingrese un DNI: "))
        print("===================")
        cursor.execute(f"SELECT socios.nombre, socios.apellido, socios.dni, socios.domicilio, socios.telefono, categoria.categoria FROM socios INNER JOIN categoria ON socios.categoria = categoria.idcategoria WHERE dni = %s",(a,))
        data=cursor.fetchall()
        for x in data:
            print("NOMBRE:",x[0],"\nAPELLIDO:",x[1],"\nDNI:",x[2],"\nDOMICILIO:",x[3],"\nTELEFONO:",x[4],"\nCATEGORIA:",x[5])

def insert():
    print("====================================")
    print((name)+", "+"has Seleccionado INGRESAR DATOS")
    print("====================================\n")

    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("===== TABLAS =====")
            print("1-> SOCIOS")
            print("2-> CATEGORIA")
            print("3-> COUTAS")
            print("4-> COBROS")
            print("5-> SALIR")
            print("=================")

            opcion = int(input((name)+", "+"Por Favor, Seleccione una opción: "))
            if opcion < 1 or opcion >5:
                print("Opción incorrcta, ingrese nuevamente...")
                print("=========================================")
            elif opcion==1:
                ##### SOCIOS #####
                print("===================================")
                print((name)+", "+"has Seleccionado SOCIOS")
                print("====================================\n")

                nombre = input("Por Favor, Ingrese un nombre: ")
                apellido= input("Por Favor, Ingrese un apellido: ")
                dni= int(input("Por Favor, Ingrese un dni: "))
                fecha= input("Por Favor, Ingrese un fechanacimiento: ")
                domicilio= input("Por Favor, Ingrese un domicilio: ")
                telefono= int(input("Por Favor, Ingrese un telefono: "))
                categoria= int(input("Por Favor, Ingrese un categoria: "))

                socios="INSERT INTO socios (nombre, apellido, dni, fechanacimiento, domicilio, telefono, categoria)\
                VALUES ('{0}', '{1}', '{2}','{3}', '{4}','{5}','{6}')".format(nombre, apellido, dni, fecha, domicilio, telefono, categoria)
                cursor.execute(socios)
                conexion.commit()

                print("=======================")
                print("Ingresado Correctamente")
                print("=======================\n")

            elif opcion==2:
                ##### CATEGORIA ######
                print("===================================")
                print((name)+", "+"has Seleccionado CATEGORIA")
                print("====================================\n")

                categoria = input("Por Favor, Ingrese una categoria: ")
                importe= input("Por Favor, Ingrese un importe: ")

                cat="INSERT INTO categoria (categoria, importe_categoria)\
	            VALUES ('{0}','{1}')".format(categoria,importe)
                cursor.execute(cat)
                conexion.commit()

                print("=======================")
                print("Ingresado Correctamente")
                print("=======================\n")

            elif opcion==3:
                ##### COBROS ######
                print("===================================")
                print((name)+", "+"has Seleccionado COBROS")
                print("====================================\n")

                mes = input("Por Favor, Ingrese una fecha: ")
                año= input("Por Favor, Ingrese una fecha: ")
                fecha= input("Por Favor, Ingrese una fecha: ")
                importe= input("Por Favor, Ingrese un importe: ")

                cobros="INSERT INTO cobros (mes, año, fechacobro, importe) \
	            VALUES ('{0}', '{1}', '{2}','{3})".format(mes,año,fecha,importe)
                cursor.execute(cobros)
                conexion.commit()

                print("=======================")
                print("Ingresado Correctamente")
                print("=======================\n")

            elif opcion==4:
                ##### COUTAS #####
                print("===================================")
                print((name)+", "+"has Seleccionado CUOTAS")
                print("====================================\n")

                mes = input("Por Favor, Ingrese una fecha: ")
                año= input("Por Favor, Ingrese una fecha: ")
                importe= input("Por Favor, Ingrese un importe: ")
        
                cuotas="INSERT INTO cuotas (mes, año, importe) \
                VALUES ('{0}', '{1}', '{2}')".format(mes,año,importe)
                cursor.execute(cuotas)
                conexion.commit()

                print("=======================")
                print("Ingresado Correctamente")
                print("=======================\n")

            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break
            else:
                print(("Error..."))
                opcionCorrecta = True

def update():
    print("====================================")
    print((name)+", "+"has Seleccionado MODIFICAR DATOS")
    print("====================================\n")

    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("===== TABLAS =====")
            print("1-> SOCIOS")
            print("2-> CATEGORIA")
            print("3-> COUTAS")
            print("4-> COBROS")
            print("5-> SALIR")
            print("=================")

            opcion = int(input((name)+", "+"Por Favor, Seleccione una opción: "))
            if opcion < 1 or opcion >5:
                print("Opción incorrcta, ingrese nuevamente...")
                print("=========================================")
            elif opcion==1:
                ##### SOCIOS #####
                print("===================================")
                print((name)+", "+"has Seleccionado SOCIOS")
                print("====================================\n")
                continuar = True
                while(continuar):
                    opcionCorrecta = False
                    while(not opcionCorrecta):
                        sql="SELECT * FROM socios"
                        cursor.execute(sql)
                        data=cursor.fetchall()
                        for x in data:
                            print("NOMBRE:",x[1],"APELLIDO:",x[2],"DNI:",x[3],"DOMICILIO:",x[5],"TELEFONO:",x[6])
                        print("\n======================")
                        print("¿Que Desea Actualizar?")
                        print("======================")
                        print("1-> Nombre")
                        print("2-> Apellido")
                        print("3-> Domicilio")
                        print("4-> Telefono")
                        print("5-> SALIR")
                        print("=====================")
                        op=int(input((name)+", "+"Por Favor, Seleccione una opción: "))
                        if opcion < 1 or opcion >5:
                            print("Opción incorrcta, ingrese nuevamente...")
                            print("=========================================")
                        elif op ==1:

                            new=input("Ingrese el Nuevo Nombre: ")
                            id=input("Ingrese un DNI ")
                            sql = "UPDATE socios SET nombre = '{}' WHERE dni = '{}'".format(new,id)
                            cursor.execute(sql)
                            conexion.commit()

                            print("===============================")
                            print("Se Ha Actualizado Correctamente")
                            print("===============================\n")

                        elif op==2:

                            new=input("Ingrese el Nuevo Apellido: ")
                            id=input("Ingrese un DNI ")
                            sql = "UPDATE socios SET apellido = '{}' WHERE dni = '{}'".format(new,id)
                            cursor.execute(sql)
                            conexion.commit()

                            print("===============================")
                            print("Se Ha Actualizado Correctamente")
                            print("===============================\n")
                        elif op==3:

                            new=input("Ingrese La nueva direccion: ")
                            id=input("Ingrese un DNI ")
                            sql = "UPDATE socios SET domicilio = '{}' WHERE dni = '{}'".format(new,id)
                            cursor.execute(sql)
                            conexion.commit()

                            print("===============================")
                            print("Se Ha Actualizado Correctamente")
                            print("===============================\n")
                        elif op==4:

                            new=input("Ingrese El Nuevo Telefono: ")
                            id=input("Ingrese un DNI ")
                            sql = "UPDATE socios SET telefono = '{}' WHERE dni = '{}'".format(new,id)
                            cursor.execute(sql)
                            conexion.commit()

                            print("===============================")
                            print("Se Ha Actualizado Correctamente")
                            print("===============================\n")

                        elif op == 5:
                            continuar = False
                            menuPrincipal()
                            break
                        else:
                            print(("Error..."))
                            opcionCorrecta = True

            elif opcion==2:
                ##### CATEGORIA ######
                print("===================================")
                print((name)+", "+"has Seleccionado CATEGORIA")
                print("====================================\n")

                new=input("Ingrese el nuevo importe: ")
                id=input("Ingrese una categoria (a o b) ")
                sql = "UPDATE categoria SET importe = '{}' WHERE categoria = '{}'".format(new,id)
                cursor.execute(sql)
                conexion.commit()

                print("===============================")
                print("Se Ha Actualizado Correctamente")
                print("===============================\n")

            elif opcion==3:
                ##### CUOTAS ######
                print("===================================")
                print((name)+", "+"has Seleccionado CUOTAS")
                print("====================================\n")

                new=input("Ingrese el nuevo valor a cambiar: ")
                id=input("Ingrese un numero ")
                sql = "UPDATE cuotas SET importe = '{}' WHERE numsocio = '{}'".format(new,id)
                cursor.execute(sql)
                conexion.commit()

                print("===============================")
                print("Se Ha Actualizado Correctamente")
                print("===============================\n")

            elif opcion==4:
                ##### COBROS #####
                print("===================================")
                print((name)+", "+"has Seleccionado COBROS")
                print("====================================\n")

                new=input("Ingrese el nuevo valor a cambiar: ")
                id=input("Ingrese un numero ")
                sql = "UPDATE cobros SET importe = '{}' WHERE numsocio = '{}'".format(new,id)
                cursor.execute(sql)
                conexion.commit()

                print("===============================")
                print("Se Ha Actualizado Correctamente")
                print("===============================\n")

            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break
            else:
                print(("Error..."))
                opcionCorrecta = True

def delete():
    print("====================================")
    print((name)+", "+"has Seleccionado BORRAR DATOS")
    print("====================================\n")

    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("===== TABLAS =====")
            print("1-> SOCIOS")
            print("2-> CATEGORIA")
            print("3-> COUTAS")
            print("4-> COBROS")
            print("5-> SALIR")
            print("=================")

            opcion = int(input((name)+", "+"Por Favor, Seleccione una opción: "))
            if opcion < 1 or opcion >5:
                print("Opción incorrcta, ingrese nuevamente...")
                print("=========================================")
            elif opcion==1:
                ##### SOCIOS #####
                print("===================================")
                print((name)+", "+"has Seleccionado SOCIOS")
                print("====================================\n")

                n=input(("Ingrese un DNI: "))
                sql="DELETE FROM socios WHERE dni = '{0}'".format(n)
                cursor.execute(sql)
                conexion.commit()

                print("=======================")
                print("Se Ha Eliminado Correctamente")
                print("=======================\n")

            elif opcion==2:
                ##### CATEGORIA ######
                print("===================================")
                print((name)+", "+"has Seleccionado CATEGORIA")
                print("====================================\n")

                n=input(("Ingrese una categoria (A o B): "))
                sql="DELETE FROM categoria WHERE categoria = '{0}'".format(n)
                cursor.execute(sql)
                conexion.commit()

                print("=======================")
                print("Se Ha Eliminado Correctamente")
                print("=======================\n")

            elif opcion==3:
                ##### CUOTAS ######
                print("===================================")
                print((name)+", "+"has Seleccionado CUOTAS")
                print("====================================\n")

                n=input(("Ingrese un ID: "))
                sql="DELETE FROM cuotas WHERE numsocio = '{}'".format(n)
                cursor.execute(sql)
                conexion.commit()

                print("=======================")
                print("Se Ha Eliminado Correctamente")
                print("=======================\n")

            elif opcion==4:
                ##### COBROS #####
                print("===================================")
                print((name)+", "+"has Seleccionado COBROS")
                print("====================================\n")

                n=input(("Ingrese un ID: "))
                sql="DELETE FROM cobros WHERE numsocio = '{}'".format(n)
                cursor.execute(sql)
                conexion.commit()

                print("=======================")
                print("Se Ha Eliminado Correctamente")
                print("=======================\n")

            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break
            else:
                print(("Error..."))
                opcionCorrecta = True

def menuPrincipal():
    print("\n######################################")
    print("Hola"+" "+(name)+", "+"Que Tengas Un Lindo Dia :)")
    print("######################################\n")

    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("========== MENÚ PRINCIPAL ==========")
            print("1-> MOSTRAR DATOS")
            print("2-> INGRESAR DATOS")
            print("3-> MODIDICAR DATOS")
            print("4-> BORRAR DATOS")
            print("5-> SALIR")
            print("====================================")

            opcion = int(input((name)+", "+"Por Favor, Seleccione una opción: "))

            if opcion < 1 or opcion >5:
                print("Opción incorrcta, ingrese nuevamente...")
                print("=========================================")
            elif opcion == 5:

                """ SORRY, HACE 3 AÑOS ESTABA ABURRIDO Y JUGABA CON EL CODIGO JAJA """

                op=input("¿Estas Seguro Que Deseas Salir?")
                if op=="si":
                    op=input("¿Estas Seguro?")
                    if op=="si":
                        op=input("¿Deverita me lo juras?")
                        if op=="si":
                            op=input("¿No me estas mientiendo, verdad?")
                            if op=="si":
                                continuar = False
                                print("¡Gracias, Nos Vemos, Vuelva Pronto!")
                                print("===================================")
                                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):

    if opcion==1:
        try:
            select()
        except:
            print("Ha Ocursorrido Un Error...")
    elif opcion==2:
        try:
            insert()
        except:
            print("Ha Ocursorrido Un Error...")
    elif opcion==3:
        try:
            update()
        except:
            print("Ha Ocursorrido Un Error...")
    elif opcion==4:
        try:
            delete()
        except:
            print("Ha Ocursorrido Un Error...")
    else:
        print("Opción no válida...")
        
menuPrincipal()
