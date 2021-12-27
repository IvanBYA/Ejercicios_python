# Sistema el cual pedirá el nombre del Alumno y seguido pedira el numero de calificaciones las cuales se van a promediar
# El usuario podra escribir una de las 2 opciones disponibles, 
# 1.- Si 
# 2.- No
# Si el usuario escribe otra opción aparecerá un error y le preguntará de nuevo la opcion hasta que escogá una opcion valida

while(True):
    respuesta = input("¿Quieres calcular un promedio de calificaciones? (si/no): ").lower()
    if(respuesta == "si"):
        resultado = 0
        nombreAlumno = input("Ingrese su nombre: ")
        cantCalificaciones = int(input("Ingrese las calificaciones a promediar: "))
        for calif in range(1,cantCalificaciones+1,1):
            calificacion = int(input(f'Ingrese la calificacion num {calif}: '))
            resultado += calificacion
        promedio = resultado / cantCalificaciones
        print("Tu nombre es: " + str(nombreAlumno) + " y tu promedio es de: " + str(promedio))
        print("")
    elif(respuesta == "no"):
        print("")
        print("Saliendo del sistema...")
        break
    else:
        print("")
        print("Escriba una de las opciones mostradas...")
        print("")

