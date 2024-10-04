import spacy
nlp = spacy.load('fr_core_news_sm')

def process_user_message(message):
    doc = nlp(message)
    # Analyse du message pour déterminer l'intention
    if 'solde' in message:
        return "Votre solde est de 1 000 EUR."
    elif 'transaction' in message:
        return "Que souhaitez-vous savoir sur vos transactions ?"
    else:
        return "Je n'ai pas compris votre demande."
