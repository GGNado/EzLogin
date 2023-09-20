def registrazione(dizionario_utenti: list):
    nome: str = input("Inserisci il tuo username: ")
    psw: str = input("Inserisci password: ")

    for utente in dizionario_utenti:
        if utente["nome"] == nome:
            print(f"""
            {'-'*12}
            Utente già registrato
            {'-'*12}
            """)
            return

    dizionario_utenti.append({"nome": nome, "password": psw})
    print("-" * 10)
    print("Registrato con successo")
    print("-" * 10)

def login(dizionario_utenti: list):
    nome: str = input("Inserisci il tuo username: ")
    psw: str = input("Inserisci password: ")

    for utente in dizionario_utenti:
        if utente["nome"] == nome and utente["password"] == psw:
            print("-"* 10)
            print("Loggato con successo")
            print("-" * 10)
            return

    print("Utente/password sbagliati o non presenti")

utenti = [
    {
        "nome": "admin",
        "password": "admin",
    },
    {
        "nome": "Papera",
        "password": "1234",
    }]

#print(type(utenti))

while True:
    x = int(input("[0] - Registrati\n[1] - Logga\n"))
    if x == 0:
        registrazione(utenti)
    elif x == 1:
        login(utenti)
    else:
        print(utenti)