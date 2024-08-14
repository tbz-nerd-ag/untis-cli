import webuntis, os, helpt
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

print("TBZ Mitte Untis CLI v0.2b\nby ingressy\n")
print("use help für Hilfe lol")

while True:
        cli = input("ingressy@untis ~$ ")

        if cli == "allclass":
                for klasse in s.klassen():
                        print(klasse.name)
        elif cli == "allrooms":
                for raum in s.rooms():
                        print(raum.name)
        elif cli == "allteachers":
                choose = input("Kuerzel oder Voller Name\n"
                                "k | v ~$ ")
                if choose == "v":
                        for lehrer in s.teachers():
                                print(lehrer.full_name)
                elif choose == "k":
                        for lehrer in s.teachers():
                                print(lehrer.name)
                else:
                        False

        elif cli == "exit":
                break
        elif cli == "help":
                helpt.help_text()
        else:
                print("Please, try again ^^")
