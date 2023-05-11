import re
import matplotlib.pyplot as plt

# Spécifiez le chemin d'accès complet de votre fichier exporté
file_path = '/Users/nilsonsimao/Downloads/isp.txt'

# Importation des données depuis le fichier exporté
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Traitement des données
participants = set()
message_count = {}

for line in data:
    # Utilisation d'une expression régulière pour extraire les noms des participants
    match = re.search(r'^\[(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})\] (.+?):', line)
    if match:
        timestamp = match.group(1)
        participant = match.group(2)
        participants.add(participant)
        message_count[participant] = message_count.get(participant, 0) + 1

# Affichage des statistiques
for participant, count in message_count.items():
    print(f"{participant}: {count} messages")

# Exemple de visualisation des résultats avec Matplotlib

participants = list(participants)
message_counts = [message_count[participant] for participant in participants]

plt.bar(participants, message_counts)
plt.xlabel('Participants')
plt.ylabel('Nombre de messages')
plt.title('Statistiques des messages')
plt.xticks(rotation=90)  # This will rotate the x-axis labels to make them more readable
plt.show()
