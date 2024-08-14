import webuntis, os, helpt, datetime
from dotenv import load_dotenv
from prettytable import prettytable, PrettyTable

load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')

s = webuntis.Session(
        server=SRV,
        username=USR,
        password=PWD,
        school=SHO,
        useragent=USRA
    )

s.login()

print("TBZ Mitte Untis CLI v0.3\nby ingressy\n")


while True:
        cli = input("ingressy@untis ~$ ")

        if cli == "allclasses":
                for klasse in s.klassen():
                        print(klasse.name)
        elif cli == "allrooms":
                for raum in s.rooms():
                        print(raum.name)
        elif cli == "allteachers":
                choose = input("Kuerzel, Voller Name oder eine Liste\n"
                                "k | v | l ~$ ")
                if choose == "v":
                        for lehrer in s.teachers():
                                print(lehrer.full_name)
                elif choose == "k":
                        for lehrer in s.teachers():
                                print(lehrer.name)
                elif choose == "l":
                        table = PrettyTable
                        for lehrer in s.teachers():
                                table.add_column([0], "Kürzel",[lehrer.name])
                                table.add_column("Voller Name",[lehrer.full_name])
                else:
                        False
        elif cli == "timetable":
                today = datetime.date.today()
                monday = today - datetime.timedelta(days=today.weekday())
                friday = monday + datetime.timedelta(days=4)

                klasse = s.klassen().filter(name="BGT 241")[0]
                tt = s.timetable(klasse=klasse, start=monday, end=friday)
                print(tt)
        elif cli == "exit":
                s.logout()
                break
        elif cli == "help":
                helpt.help_text()
        else:
                print("Please, try again ^^")
