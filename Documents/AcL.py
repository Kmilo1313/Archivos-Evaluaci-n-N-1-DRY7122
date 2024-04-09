def determinar_tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

try:
    numero_acl = int(input("Introduce el número de ACL IPv4: "))
    tipo_acl = determinar_tipo_acl(numero_acl)
    print("El número de ACL IPv4", numero_acl, "corresponde a una", tipo_acl)
except ValueError:
    print("Error: Debes ingresar un número válido de ACL IPv4.")
