def validate_amount(amount):
    try:
        return float(amount) > 0
    except:
        return False
