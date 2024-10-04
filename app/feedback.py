from app.models import Feedback
from . import db

def save_feedback(user_id, feedback_text):
    feedback = Feedback(user_id=user_id, feedback_text=feedback_text)
    db.session.add(feedback)
    db.session.commit()
    return "Votre feedback a été enregistré, un conseiller vous contactera si nécessaire."
