import webuntis, os
from dotenv import load_dotenv


load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')

s = webuntis.Session(
        server=(SRV),
        username=(USR),
        password=(PWD),
        school=(SHO),
        useragent=(USRA)
    )

s.login()

print("TBZ Mitte Untis CLI\nby ingressy\n")
print("[0] = Alle Klassen anzeigen")

while True:
        cli = input("ingressy@untis ~$ ")

        if cli == "1":
                for klasse in s.klassen():
                        print(klasse.name)
        else:
                print("Please, try again ^^")
