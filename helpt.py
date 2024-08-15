import os
from dotenv import load_dotenv

load_dotenv()
STS = os.getenv('STS')

def help_text():
    print("allclass     | Zeigt dir alle Klassen am TBZ an")
    print("allrooms     | Zeigt dir alle Räume am TBZ an")
    print("allteachers  | Zeigt dir alle Lehrer am TBZ an")
    print("help         | Zeigt diese Informationen an")
    print("rooms        | Zeigt dir den Belegungsplan eines Raumes an")
    print("timetable    | Zeigt dir einen Stundenplan einer Klasse an")

