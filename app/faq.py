def get_faq_answer(question):
    faqs = {
        "Comment ouvrir un compte ?": "Vous pouvez ouvrir un compte en ligne ou en agence.",
        "Quels sont les frais de maintenance ?": "Les frais de maintenance sont de 10 EUR par mois.",
    }
    
    return faqs.get(question, "Je ne connais pas la réponse à cette question.")
