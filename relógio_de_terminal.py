from datetime import datetime
import time
import os

def relogio_terminal():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            agora = datetime.now()
            hora = agora.strftime("%H:%M:%S")
            data = agora.strftime("%d/%m/%Y")
            print(f"Hoje é: {data}")
            print(f"A hora atual é: {hora}")
            print("Pressione Ctrl+c para sair.")
            time.sleep(1)  # Aguarda 1 segundo antes de atualizar
    except KeyboardInterrupt:
        print("\nRelógio de terminal encerrado.")

relogio_terminal()