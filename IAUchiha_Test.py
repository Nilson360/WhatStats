
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models.ldamodel import LdaModel
import re
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

# Définition des stopwords en portugais
stop_words = set(stopwords.words('portuguese'))

# Importation des données depuis le fichier exporté
file_path = '/Users/nilsonsimao/Downloads/_chat3.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Traitement des données
messages_per_month = defaultdict(list)

for line in data:
    match = re.search(r'^\[(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2})\] (.+?): (.*)', line)
    if match:
        timestamp = match.group(1)
        message = match.group(3)
        month = timestamp[3:10]  # Extraire le mois et l'année
        messages_per_month[month].append(message)

# Analyse de sujet pour chaque mois
for month, messages in messages_per_month.items():
    # Préparation des données pour l'analyse de sujet
    documents = []
    for message in messages:
        # Tokenisation et suppression des stopwords
        words = [word for word in word_tokenize(message) if word not in stop_words]
        documents.append(words)

    # Création d'un dictionnaire à partir de la liste de documents
    dictionary = corpora.Dictionary(documents)

    # Création d'un "corpus" à partir de la liste de documents
    corpus = [dictionary.doc2bow(doc) for doc in documents]

    # Entraînement du modèle LDA
    lda_model = LdaModel(corpus, num_topics=10, id2word=dictionary)

    # Impression des sujets
    print(f"Month: {month}")
    for i, topic in lda_model.print_topics(-1):
        print(f"  Topic: {i} \n  Words: {topic}")
