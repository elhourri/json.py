import json

data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

try:
    with open("data.json", "r") as json_file:
        initial_data = json.load(json_file)
        print("Contenu du fichier initial:")
        print(initial_data)

    initial_data["language"] = "Python"

    with open("data.json", "w") as json_file:
        json.dump(initial_data, json_file, indent=2)

    with open("data.json", "r") as json_file:
        new_data = json.load(json_file)
        print("\nContenu du fichier après modification:")
        print(new_data)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
except json.JSONDecodeError:
    print("Erreur de décodage JSON.")
