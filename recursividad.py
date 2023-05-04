'''
Alumno : Rodríguez Ramírez Brandon Alan
6to semestre, TM.
'''
def E():
    global i
    if T():
        if E_():
            return True
        else:
            return False
    else:
        return False

def E_():
    global i
    if i < len(cadena) and cadena[i] == '+':
        i += 1
        if T():
            if E_():
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def T():
    global i
    if F():
        if T_():
            return True
        else:
            return False
    else:
        return False

def T_():
    global i
    if i < len(cadena) and cadena[i] == '*':
        i += 1
        if F():
            if T_():
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def F():
    global i
    if i < len(cadena):
        if cadena[i] == '(':
            i += 1
            if E():
                if i < len(cadena) and cadena[i] == ')':
                    i += 1
                    return True
                else:
                    return False
            else:
                return False
        elif cadena[i] == 'i':
            i += 1
            return True
        else:
            return False
    else:
        return False

# Ejemplo de uso
# cadena = "i+(i*i)"
salir = 0
while salir != 1:
    cadena = input("Ingresa la cadena: ")
    i = 0
    if E() and i == len(cadena):
        print("La cadena es válida.")
    else:
        print("La cadena no es válida.")
    print("Desea salir del programa?\n1-->Si\n2-->No")   
    salir = int(input("Opcion->"))

def generarArbol():
    arbol = ""
    
    return arbol