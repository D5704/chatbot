from app.models import User, Transaction
from . import db

def process_transaction(user_id, transaction_type, amount):
    user = User.query.get(user_id)
    if transaction_type == 'deposit':
        user.account_balance += amount
    elif transaction_type == 'withdraw':
        user.account_balance -= amount
    
    # Sauvegarder la transaction dans la base de données
    new_transaction = Transaction(user_id=user_id, amount=amount, transaction_type=transaction_type)
    db.session.add(new_transaction)
    db.session.commit()

    return user.account_balance
