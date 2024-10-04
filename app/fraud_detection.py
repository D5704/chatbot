def detect_fraud(transaction):
    if transaction.amount > 10000:
        return True
    return False
