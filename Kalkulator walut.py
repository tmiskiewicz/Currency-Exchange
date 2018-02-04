import urllib.request
import json

dane = urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a/?format=json")

dokument = json.loads(dane.read())

global_ccy = {}

def list_of_currency():
    
    ile = len(dokument[0]["rates"])
    
    for i in range(ile):
        currency = dokument[0]["rates"][i]["currency"]
        mid = float(dokument[0]["rates"][i]["mid"])
        global_ccy.update({currency:mid})
        

def text_interface():
    while True:
        print('\nWelcome to currency exchange. What would like to do ? ' + \
              '\nExchange PLN to another currency (enter: p) ' + \
              '\nExchange some currency to PLN (enter: c)' + \
              '\nFinish your transaction (enter: q)')
        
        decision = input()
        if decision == 'q':
            print('Thank you for using our services')
            break
        elif decision == 'p':
            print(f'Below you can find avaiable currency and their exchange rate: ')
            print(global_ccy)
            
            name_of_currency = input('Please, give the name of currency: ')
            amount = int(input('Please, give the amount that you want to change: '))
            result = round(amount / global_ccy[name_of_currency], 2)
            print(f'\nYou changed {amount} PLN to {result} {name_of_currency}')
        elif decision == 'c':
            print(f'Below you can find avaiable currency and their exchange rate: ')
            print(global_ccy)
            
            name_of_currency = input('Please, give the name of currency ' +\
                                     ' that you own: ')
            amount = int(input('Please, give the amount that you want to change: '))
            result = round(amount * global_ccy[name_of_currency], 2)
            print(f'\nYou changed {amount} {name_of_currency} to {result} PLN')
        elif decision != 'p' or 'c':
                print("Sorry, but we can't change this currency. Please check your " + \
                      " spelling")
        
               
list_of_currency()
text_interface()
    
    

