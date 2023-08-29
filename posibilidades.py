import itertools
from validador import validate_option

nodos = {
    0: "mobile phone",
    1: "calls",
    2: "gps",
    3: "screen",
    4: "media",
    5: "basic",
    6: "color",
    7: "hires",
    8: "camera",
    9: "mp3"
}

mapa = {
    0: [(1, "m"), (2, "opt"), (3, "m"), (4, "opt")],
    1: [],
    2: [(5, "ex")],
    3: [(5, "alt"), (6, "alt"), (7, "alt")],
    4: [(8, "or"), (9, "or")],
    5: [(2, "ex")],
    6: [],
    7: [],
    8: [(7, "req")],
    9: []
}

base = [0] # Siempre considerar el primero
opciones = list(mapa.keys())[1:]

combinations = []
valid = []

# Generar todas las combinaciones posibles
for r in range(1, len(opciones) + 1):
    combinations.extend(itertools.combinations(opciones, r))


print("Number of combinations: {}".format(len(combinations)))
for combo in combinations:
    option = base + list(combo)
    print("Checking option '{}': ".format(option), end="")
    if validate_option(option, mapa, nodos):
        print("Valid! :D")
        valid.append(option)

print("\nNumber of valid combinations: {}\n".format(len(valid)))
for val in valid:
    print(", ".join(nodos[item] for item in val[1:-1]) + " and {}".format(nodos[val[-1]]))
