import os
from dotenv import load_dotenv

load_dotenv()
STS = os.getenv('STS')

def help_text():
    print("all          | Gives you a small sub programme with which you can display a lot of information")
    print("doorsign     | Gives you a table of the current hour")
    print("help         | Shows you this information")
    print("rooms        | Shows you the occupancy plan of a room")
    print("timetable    | Shows you a timetable of a class")

