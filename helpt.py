import os
from dotenv import load_dotenv

load_dotenv()
STS = os.getenv('STS')

def help_text():
    print("allclass     | Zeigt dir alle Klassen am TBZ an")
    print("allrooms     | Zeigt dir alle Räume am TBZ an")
    print("allteachers  | Zeigt dir alle Lehrer am TBZ an")
    print("help         | Zeigt diese Informationen an")
    if STS == "dev":
        print("timetable    | Zeigt einen Unlesbaren Stundenplan an")
    else:
        print("Bei Problemen und Anregungen, gerne eine Issuse bei Github öffnen.")

