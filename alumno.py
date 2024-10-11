from alo import Alumno

alumnos_dict = {}

# Bucle para ingresar hasta 50 alumnos
for i in range(3):
    print(f"\n--- Ingreso de Alumno {i} ---")

    alumno = Alumno()

    nombre = input("Ingrese el nombre: ")
    apellido_paterno = input("Ingrese el apellido paterno: ")
    apellido_materno = input("Ingrese el apellido materno: ")
    no_control = input("Ingrese el número de control: ")
    semestre = input("Ingrese el semestre: ")

    # Almacenar la instancia en el diccionario
    alumnos_dict[i] = alumno
    print(f"nombre: {alumnos_dict[0].get_nombre()}")

    # Establecer valores en la instancia de Alumno
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

#mostrar los nombres registrados
for i in range(3):
    print(f"Nombre:{alumnos_dict[i].get_nombre()}")



# Mostrar información de todos los alumnos almacenados
print("\n--- Información de Alumnos ---")
for clave, alumno in alumnos_dict.items():
    print(f"\nAlumno {clave}:")
    print(alumno.mostrar_info())