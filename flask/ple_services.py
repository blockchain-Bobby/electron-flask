import requests as r

def get_info():
    result = r.get('https://cache.pleapps.plenteum.com/info')
    return result

def domain_registration_payment():
    turtle_pay = 'https://api.turtlepay.io/v1/new'
    tx_details ={
        'address': 'TRTLuwh9Jfx4nhzmsZwaciNVPUMYxicu4XNUT4X9pwBaN5gsBTGDEHFHTVTtDrAu9A5TP3RBqAGjJTb6RC2FEsJPCogz4m7cbhw',
        'amount': 10000,
        'callback': '',
        'confirmations': 60,
        'userDefined':{}
        }
        #add in callback"
    payment_details = r.post(turtle_pay, json=tx_details)
    return payment_details

def asset_registration_payment():
    turtle_pay = 'https://api.turtlepay.io/v1/new'
    tx_details ={
        'address': 'TRTLuwh9Jfx4nhzmsZwaciNVPUMYxicu4XNUT4X9pwBaN5gsBTGDEHFHTVTtDrAu9A5TP3RBqAGjJTb6RC2FEsJPCogz4m7cbhw',
        'amount': 1000,
        'callback': '',
        'confirmations': 60,
        'userDefined':{}
        }
        #add in callback"
    payment_details = r.post(turtle_pay, json=tx_details)
    return payment_details