from tkinter import Tk, Canvas, simpledialog
from datetime import date, datetime

def get_event():
    list_events = []
    with open("event.py") as file:
        for line in file:
            line = line.rstrip("\n")
            current_event = line.split(",")
            event_date = datetime.strptime(current_event[1], "%d/%m/%y").date()
            current_event[1] = event_date
            list_events.append(current_event)
            print(list_events)
    return list_events

def day_between_dates(date1, date2):
    time_between = str(date1-date2)
    num_of_days = time_between.split (",")
    return(num_of_days[0])

window = Tk()
c = Canvas(window,width=1000,height=800, bg='lavender')
c.pack()
c.create_text(100,59,fill='purple',text='Calender',font='Arial 30')

events = get_event()
today = date.today()
vertical_space = 150
for event in events:
    event_name = event[0]
    days_until = day_between_dates(event[1],today)
    display = "%s ~ %s Left"%(event_name, days_until)
    c.create_text(100,vertical_space,fill="white",text=display,font='Courier 26',anchor='w')
    vertical_space = vertical_space + 59
