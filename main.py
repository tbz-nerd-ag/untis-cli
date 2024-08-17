import datetime, helpt, os, webuntis.objects, logging

from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')
STS = os.getenv('STS')

s = webuntis.Session(
        server=SRV,
        username=USR,
        password=PWD,
        school=SHO,
        useragent=USRA
    )

s.login()

print("TBZ Mitte Untis CLI v0.4\nby ingressy\n")


while True:
        cli = input("ingressy@untis ~$ ")

        if cli == "allclasses":
                for klasse in s.klassen():
                        print(klasse.name)
        elif cli == "allrooms":
                for raum in s.rooms():
                        print(raum.name)
        elif cli == "allstudents":
                for schueler in s.students():
                        print(schueler.id)
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
                        if STS == "dev":
                                table = PrettyTable
                                for lehrer in s.teachers():
                                        table.add_column([0], "Kürzel",[lehrer.name])
                                        table.add_column([1],"Voller Name",[lehrer.full_name])
                        else:
                                print("Diese Funktion ist noch in der Entwichklung!")
                else:
                        False
        elif cli == "timetable":
                choose = input("Von welcher Klasse möchtest du den Stundenplan haben? ")

                today = datetime.date.today()
                monday = today - datetime.timedelta(days=today.weekday())
                friday = monday + datetime.timedelta(days=4)

                klasse = s.klassen().filter(name=choose)
                tt = s.timetable(klasse=klasse[0], start=monday, end=friday)
                tt = sorted(tt, key=lambda x: x.start)
                #print(tt)

                time_format_end = "%H:%M"
                time_format_start = "%Y-%m-%d %a " + time_format_end

                table = PrettyTable()
                table.field_names = ["Anfang", "Ende", "Klasse", "Lehrer", "Raum", "Fach"]

                for po in tt:
                        s = po.start.strftime(time_format_start)
                        e = po.end.strftime(time_format_end)
                        k = " ".join([k.name for k in po.klassen])
                        #t = " ".join([t.name for t in po.teachers])
                        r = " ".join([r.name for r in po.rooms])
                        sub = " ".join([r.name for r in po.subjects])
                        c = "(" + po.code + ")" if po.code is not None else ""
                        # print(s + "-" + e, k, sub, t, r, c)

                        table.add_row([s, e, k, "t", r, sub])
                print(table)

        elif cli == "rooms":
                choose = input("Von welchen Raum möchtest du den Stundenplan haben? ")

                start = datetime.datetime.now()
                end = start + datetime.timedelta(days=5)

                rooms = s.rooms().filter(name=choose)

                tt = s.timetable(room=rooms[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)
                #print(tt)

                time_format_end = "%H:%M"
                time_format_start = "%Y-%m-%d %a " + time_format_end

                table = PrettyTable()
                table.field_names = ["Anfang","Ende", "Klasse", "Lehrer", "Raum", "Fach"]

                for po in tt:
                       s = po.start.strftime(time_format_start)
                       e = po.end.strftime(time_format_end)
                       k = " ".join([k.name for k in po.klassen])
                       t = " ".join([t.name for t in po.teachers])
                       r = " ".join([r.name for r in po.rooms])
                       sub = " ".join([r.name for r in po.subjects])
                       c = "(" + po.code + ")" if po.code is not None else ""
                       #print(s + "-" + e, k, sub, t, r, c)

                       table.add_row([s,e, k, t, r, sub])
                print(table)
        elif cli == "doorsign":
                choose = input("Von welchen Raum möchtest du den Stundenplan haben? ")
                choose1 = input("An welchen Tag den? ")
                choose2 = input("Um welche Uhrzeit? ")

                start = datetime.datetime.now()
                end = start + datetime.timedelta(days=5)

                rooms = s.rooms().filter(name=choose)

                tt = s.timetable(room=rooms[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)

                time_format_end = "%H%M"
                time_format_start = "%Y-%m-%d %a " + time_format_end

                for po in tt:
                        s = po.start.strftime(time_format_start)
                        e = po.end.strftime(time_format_end)
                        k = " ".join([k.name for k in po.klassen])
                        t = " ".join([t.name for t in po.teachers])
                        r = " ".join([r.name for r in po.rooms])
                        sub = " ".join([r.name for r in po.subjects])
                        c = "(" + po.code + ")" if po.code is not None else ""
                        #print(s + "-" + e, k, sub, t, r, c)

                        #print (e)
                        if e < choose1:
                                print(s + "-" + e, k, sub, t, r, c)
                        else:
                           logging.error("Time Error")
        elif cli == "exit":
                s.logout()
                break
        elif cli == "help":
                helpt.help_text()
        else:
                print("Please, try again ^^")
