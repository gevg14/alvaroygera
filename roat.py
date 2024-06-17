def agregado_t():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    cargo = input("Ingresa tu cargo: ")
    trabajador = {
        "Nombre":nombre,
        "Apellido":apellido,
        "Cargo":cargo
    }
    if cargo=="ayudante":
        print("su cargo de ayudante es remunerado con $410.000")
    elif cargo=="trabajador fijo":
        print("su cargo de ayudante es remunerado con $750.000")
    elif cargo=="supevisor":
        print("su cargo de ayudante es remunerado con $810.000")
    elif cargo=="ceo":
        print("su cargo de ayudante es remunerado con $1.000.000")
    else:
        print("usted no es de esta empresa ")


