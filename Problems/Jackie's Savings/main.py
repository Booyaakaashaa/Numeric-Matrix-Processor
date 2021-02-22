def final_deposit_amount(*args, amount=1000):
    for i in args:
        amount = amount * (100 + i) / 100
    return round(amount, 2)
