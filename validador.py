# Chequea que una option tenga todas las mandatorias del mapa
def check_all_mandatory(option, mapa, nodos):
    for nodo in mapa[0]:
        if nodo[1] == "m":
            if nodo[0] not in option:
                print("Mandatory Error: '{} ({})' is mandatory".format(nodos[nodo[0]], nodo[0]))
                return False   
    else:
        return True
    
# Chequea que una option tenga tenga las dependencias
def check_requires(option, mapa, nodos):
    for nodo in option:
        dependencias = [item[0] for item in mapa[nodo] if item[1] == "req"]

        for dependencia in dependencias:
            if dependencia not in option:
                print("Requires Error: '{} ({})' requires '{} ({})'".format(nodos[nodo], nodo, nodos[dependencia], dependencia))
                return False
    return True

# Chequea que la option no tenga nodos que se excluyen
def check_excludes(option, mapa, nodos):
    for nodo in option:
        excludes = [item[0] for item in mapa[nodo] if item[1] == "ex"]
        for exclude in excludes:
            if exclude in option:
                print("Exclude Error: '{} ({})' excludes '{} ({})'".format(nodos[nodo], nodo, nodos[exclude], exclude))
                return False
    return True

# Chequea que se tenga solo una alternativa en nodos de alternativa
def check_alternatives(option, mapa, nodos):
    for nodo in option:
        alternatives = [item[0] for item in mapa[nodo] if item[1] == "alt"]
        if len(alternatives) > 0:
            are_in = []
            for alt in alternatives:
                if alt in option:
                    are_in.append(alt)
            if len(are_in) == 0:
                print("Alternatives Error: you need to specify the alternative for '{} ({})'".format(nodos[nodo], nodo))
                return False
            if len(are_in) > 1:
                detail = ", ".join("'{} ({})'".format(nodos[item], item) for item in are_in[:-1]) + " and '{} ({})'".format(nodos[are_in[-1]], are_in[-1])
                print("Alternatives Error: there can be only 1 alternative for '{} ({})' and there is {}".format(nodos[nodo], nodo, detail))
                return False
    return True

# Chequea que que se tenga almenos una opcion en nodos ors
def check_ors(option, mapa, nodos):
    for nodo in option:
        ors = [item[0] for item in mapa[nodo] if item[1] == "or"]
        if len(ors) > 0:
            are_in = []
            for o in ors:
                if o in option:
                    are_in.append(o)
            if len(are_in) == 0:
                print("Or error: you need to specify one or for '{} ({})'".format(nodos[nodo], nodo))
                return False
    return True

def validate_option(option, mapa, nodos):
    return check_all_mandatory(option, mapa, nodos) and check_requires(option, mapa, nodos) and check_excludes(option, mapa, nodos) and check_alternatives(option, mapa, nodos) and check_ors(option, mapa, nodos)