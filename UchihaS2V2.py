import re
import matplotlib.pyplot as plt

# Spécifiez le chemin d'accès complet de votre fichier exporté
file_path = '/Users/nilsonsimao/Downloads/_chat3.txt'

# Importation des données depuis le fichier exporté
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Traitement des données
participants_messages = {}

for line in data:
    # Utilisation d'une expression régulière pour extraire les noms des participants et leurs messages
    match = re.search(r'^\[(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})\] (.+?): (.*)', line)
    if match:
        timestamp = match.group(1)
        participant = match.group(2)
        message = match.group(3)
        if participant not in participants_messages:
            participants_messages[participant] = [message]
        else:
            participants_messages[participant].append(message)

# Calcul du nombre de messages pour chaque participant
message_counts = {participant: len(messages) for participant, messages in participants_messages.items()}

# Tri du dictionnaire par nombre de messages en ordre croissant
sorted_counts = sorted(message_counts.items(), key=lambda item: item[1])

# Sélection des 30 participants ayant le moins de messages
bottom_30 = sorted_counts[:100]

# Affichage du nombre de messages des 30 participants
for participant, count in bottom_30:
    print(f"{participant}: {count} messages")
