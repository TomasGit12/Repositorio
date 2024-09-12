def determinar_grupo(nombre, sexo):
    
    nombre = nombre.lower()
    
    
    primera_letra = nombre[0]
    
    if sexo == "F":
        
        if primera_letra < 'm':
            return "Grupo A"
        else:
            return "Grupo B"
    elif sexo == "M":
        
        if primera_letra > 'n':
            return "Grupo A"
        else:
            return "Grupo B"
    else:
        return "Sexo no válido"

def main():
    
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M para masculino, F para femenino): ").upper()
    
    
    grupo = determinar_grupo(nombre, sexo)
    
    
    print(f"Pertenece al {grupo}")

if __name__ == "__main__":
    main()
