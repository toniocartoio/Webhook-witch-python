import requests
import json
import time
import sys

# Definisci i dati del webhook
WEBHOOK_URL = 'Il Tuo Webhook'

def invia_messaggio():
    while True:
        try:
            # Chiedi all'utente quale messaggio desidera inviare
            messaggio = input("Inserisci il messaggio da inviare: ")

            # Definisci il payload del messaggio
            payload = {
                'content': messaggio
            }

            # Invia una richiesta POST al webhook
            response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

            # Controlla lo stato della risposta
            if response.status_code == 200:
                print('Messaggio inviato con successo.')
            else:
                print('Messaggio inviato con successo.')

        except Exception as e:
            print('Si è verificato un errore:', str(e))

        # Attendi 10 secondi prima di inviare il prossimo messaggio
        time.sleep(1)

# Avvia l'invio dei messaggi
if __name__ == "__main__":
    invia_messaggio()
