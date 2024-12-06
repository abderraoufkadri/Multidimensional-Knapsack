

# Lire le fichier avec encodage UTF-8
with open("instance.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Variables pour stocker les données extraites
nbr_objects = 0
nbr_resources = 0
values = []  # Liste qui contiendra [index, valeur]
consumption_matrix = []  # Matrice de consommation des ressources
capacities = []  # Capacités des ressources

# Extraire le nombre d'objets et de ressources
nbr_objects, nbr_resources = map(int, lines[1].strip().split())

# Extraire les valeurs des objets avec leurs indices
index = 3
while lines[index].strip() != "les quatités des resources consommées pour chaque objet (ligne)":
    value = int(lines[index].strip())
    values.append([index - 3, value])  # L'indice est calculé par la position dans le fichier
    index += 1

# Extraire la matrice de consommation des ressources
index += 1  # Sauter la ligne "les quatités des resources consommées pour chaque objet (ligne)"
while lines[index].strip() != "les capacités des ressources":
    row = list(map(int, lines[index].strip().split()))
    consumption_matrix.append(row)
    index += 1

# Extraire les capacités des ressources
index += 1  # Sauter la ligne "les capacités des ressources"
while index < len(lines):
    capacities.append(int(lines[index].strip()))
    index += 1

# Les variables sont maintenant remplies :
# nbr_objects : int - Nombre d'objets
# nbr_resources : int - Nombre de ressources
# values : liste de [index, valeur] - Index et valeur de chaque objet
# consumption_matrix : liste de listes - Consommation des ressources pour chaque objet
# capacities : liste d'int - Capacités de chaque ressource

# Exemple d'utilisation des variables
print("Nombre d'objets :", nbr_objects)
print("Nombre de ressources :", nbr_resources)
print("Valeurs (index et valeurs) :", values[:5])  # Afficher les 5 premiers
print("Premières 5 lignes de la matrice de consommation :", consumption_matrix[:5])
print("Capacités :", capacities)

# Calculate value-to-weight ratio for each object
value_to_weight = [
    (value[0], value[1] / sum(consumption_matrix[value[0]]), value[1])  # Use valid indices
    for value in values
]

# Sort objects by value-to-weight ratio
sorted_objects = sorted(value_to_weight, key=lambda x: x[1], reverse=True)

# Initialize remaining capacities and total score
total_score = 0
remaining_capacities = capacities[:]
selected_indices = []

# Select objects based on the value-to-weight ratio
for obj in sorted_objects:
    index, ratio, value = obj

    # Ensure the index is within range
    if index < len(consumption_matrix):
        consumption = consumption_matrix[index]

        # Check if the object fits
        if all(c >= cons for c, cons in zip(remaining_capacities, consumption)):
            # Add the object's value to the score
            total_score += value
            # Subtract its consumption from remaining capacities
            remaining_capacities = [c - cons for c, cons in zip(remaining_capacities, consumption)]
            # Store the index of the selected object
            selected_indices.append(index)

# Output final results
print("Optimized Total Score:", total_score)
print("Final Remaining Capacities:", remaining_capacities)
print("Indices of Selected Objects:", selected_indices)
