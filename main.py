import datetime, helpt, os, webuntis.objects, random

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

print("TBZ Mitte Untis CLI v0.4 \nby ingressy\n")
ramtext = ["thanks to Monster Energy and Katjes for mental support", "buy me a coffe pls ... i hate this shit", "READY.", "you are hacked", "My unicorn says: reality lies", "i like pancakes"]
print(random.choice(ramtext))

while True:
        cli = input("ingressy@untis ~$ ")
        if cli == "all":
                acli = input("ingressy@untis /all/ ~$ ")
                if acli == "classes":
                        for klasse in s.klassen():
                                print(klasse.name)
                elif acli == "rooms":
                        for raum in s.rooms():
                                print(raum.name)
                elif acli == "students":
                        for schueler in s.students():
                                print(schueler.full_name)
                elif acli == "subjects":
                        for feacher in s.subjects():
                                print(feacher.long_name)
                elif acli == "teachers":
                        choose = input("Kuerzel, Voller Name oder eine Liste\n"
                                       "k | v | l ~$ ")
                        if choose == "v":
                                for lehrer in s.teachers():
                                        print(lehrer.full_name)
                        elif choose == "k":
                                for lehrer in s.teachers():
                                        print(lehrer.name)
                        elif choose == "l":
                                table = PrettyTable()
                                table.field_names = ["Kürzel", "Voller Namen"]

                                for lehrer in s.teachers():
                                        ln = lehrer.name
                                        lf = lehrer.full_name

                                        print(lehrer.name)
                                        print(lehrer.full_name)
                        else:
                                False

        elif cli == "timetable":
                choose = input("From which class would you like to have the timetable? ")

                start = datetime.datetime.now()
                end = start + datetime.timedelta(days=4)

                klasse = s.klassen().filter(name=choose)
                tt = s.timetable(klasse=klasse[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)
                #print(tt)

                time_format_end = "%H:%M"
                time_format_start = "%Y-%m-%d %a " + time_format_end

                table = PrettyTable()
                table.field_names = ["Start", "End", "Teacher", "Room", "Subject", "News"]

                for po in tt:
                        s = po.start.strftime(time_format_start)
                        e = po.end.strftime(time_format_end)
                        k = " ".join([k.name for k in po.klassen])
                        t = " ".join([t.full_name for t in po.teachers])
                        r = " ".join([r.name for r in po.rooms])
                        sub = " ".join([r.long_name for r in po.subjects])
                        c = "(" + po.code + ")" if po.code is not None else ""
                        #print(s + "-" + e, k, sub, t, r, c)

                        table.add_row([s, e, t, r, sub, c])
                print(table)

        elif cli == "rooms":
                choose = input("From which room would you like to have the timetable? ")

                start = datetime.datetime.now()
                end = start + datetime.timedelta(days=4)

                rooms = s.rooms().filter(name=choose)

                tt = s.timetable(room=rooms[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)
                #print(tt)

                time_format_end = "%H:%M"
                time_format_start = "%Y-%m-%d %a " + time_format_end

                table = PrettyTable()
                table.field_names = ["Start","End", "Class", "Teacher", "Room", "Subject", "News"]

                for po in tt:
                       s = po.start.strftime(time_format_start)
                       e = po.end.strftime(time_format_end)
                       k = " ".join([k.name for k in po.klassen])
                       t = " ".join([t.name for t in po.teachers])
                       r = " ".join([r.name for r in po.rooms])
                       sub = " ".join([r.long_name for r in po.subjects])
                       c = "(" + po.code + ")" if po.code is not None else ""
                       #print(s + "-" + e, k, sub, t, r, c)

                       table.add_row([s,e, k, t, r, sub, c])
                print(table)
        elif cli == "doorsign":
                choose = input("From which room would you like to have the timetable? ")
                chtime = input("What time is it? ")

                start = datetime.datetime.now()
                end = start + datetime.timedelta(days=4)

                rooms = s.rooms().filter(name=choose)

                tt = s.timetable(room=rooms[0], start=start, end=end)
                tt = sorted(tt, key=lambda x: x.start)
                #print(tt)

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

                       if chtime < e:
                               print(s + "-" + e, k, sub, t, r, c)
        elif cli == "exit":
                s.logout()
                break
        elif cli == "help":
                helpt.help_text()
        else:
                print("Please, try again ^^")
