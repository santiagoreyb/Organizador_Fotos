
print("Bienvenidos a la Agenda Telefonica")
listacontactos = ["Santiago Rey", 3116310552, "calle 2a #25-30", "bien"]
respuesta = "s"
while(respuesta == "s"):
    print("Seleccione la opcion de su preferencia:) ")
    print("1. Ingresar nuevo contacto")
    print("2. Generar listados de contactos que me caen bien.")
    print("3. Generar listados de contactos que me caen mal")
    print("4. Eliminar un contacto de la agenda")
    print("5. Buscar por nombre entre los contactos")
    opcion = input()
    print("la opcion elegida es ", opcion)
    if int(opcion) == 1:
        print("ingrese el nombre del nuevo contacto")
        nombre = input()
        print("ingrese el numero del nuevo contacto")
        numero = input()
        print("ingrese la direccion del nuevo contacto")
        direccion = input()
        print("ingrese el estado del nuevo contacto(ingrese 'mal' o 'bien')")
        estado = input()
        listacontactos.append(nombre)
        listacontactos.append(int(numero))
        listacontactos.append(direccion)
        listacontactos.append(estado)
    if int(opcion) == 2:
        i = 0
        print("---Contactos que me caen bien---")
        while i+4 <= len(listacontactos):
            if listacontactos[i+3] == "bien":
                print("Nombre: ", listacontactos[i])
                print("Numero: ", listacontactos[i+1])
                print("Direccion: ", listacontactos[i+2])
                print("Estado: ", listacontactos[i+3])
            i+=1
    if int(opcion) == 3:
        i = 0
        print("---Contactos que me caen mal---")
        while i+4 <= len(listacontactos):
            if listacontactos[i+3] == "mal":
                print("Nombre: ", listacontactos[i])
                print("Numero: ", listacontactos[i+1])
                print("Direccion: ", listacontactos[i+2])
                print("Estado: ", listacontactos[i+3])
            i+=1
    if int(opcion) == 4:
        i = 0
        j = 0
        if len(listacontactos) > 0:
            print("---Contactos--")
            while i < len(listacontactos):
                if i%4 == 0:
                    print("Contacto: ", j)
                    print("Nombre: ", listacontactos[i])
                    print("Numero: ", listacontactos[i+1])
                    print("Direccion: ", listacontactos[i+2])
                    print("Estado: ", listacontactos[i+3])
                    j+=1
                i+=1
            print("Seleccione el indice del contacto a eliminar")
            i = input()
            i = int(i*4)
            listacontactos.pop(int(i))
            listacontactos.pop(int(i))
            listacontactos.pop(int(i))
            listacontactos.pop(int(i))
        else:
            print("No existen mas contactos")
    if int(opcion) == 5:
        i = 0
        print("---Contacto a buscar--")
        print("---Digite el nombre del contacto buscado--")
        name = input()
        while i < len(listacontactos):
            if name == listacontactos[i]:
                print("Nombre: ", listacontactos[i])
                print("Numero: ", listacontactos[i+1])
                print("Direccion: ", listacontactos[i+2])
                print("Estado: ", listacontactos[i+3])
            i+=1
    print("Desea continuar?(digite 's' para SI)")
    respuesta = input()
