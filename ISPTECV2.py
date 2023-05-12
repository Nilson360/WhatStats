import re
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

# Spécifiez le chemin d'accès complet de votre fichier exporté
file_path = '/Users/nilsonsimao/Downloads/_chat6.txt'

# Importation des données depuis le fichier exporté
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Traitement des données
monthly_messages = defaultdict(int)

for line in data:
    # Utilisation d'une expression régulière pour extraire les noms des participants et leurs messages
    match = re.search(r'^(\d{2}/\d{2}/\d{4} \d{2}:\d{2}) - (.+?): (.*)', line)
    if match:
        timestamp = match.group(1)
        participant = match.group(2)
        message = match.group(3)
        # Convert the timestamp string to a datetime object
        date_time_obj = datetime.strptime(timestamp, '%d/%m/%Y %H:%M')
        # Get the month and year of the message
        month_year = date_time_obj.strftime("%m/%Y")
        monthly_messages[month_year] += 1

# Tri du dictionnaire par date en ordre croissant
sorted_counts = sorted(monthly_messages.items(), key=lambda item: datetime.strptime(item[0], "%m/%Y"))

# Création du graphique
months = [item[0] for item in sorted_counts]
counts = [item[1] for item in sorted_counts]

bars = plt.bar(months, counts)
plt.xlabel('Mois')
plt.ylabel('Nombre de messages')
plt.title('Nombre de messages par mois')
plt.xticks(rotation=90)

# Ajout du nombre de messages au-dessus de chaque barre
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, yval, ha='center', va='bottom')

plt.show()
