from Meetingroom import MeetingroomInfo
import pandas_related
import TKGUI

from tkinter import *

data = pandas_related.read_data()
room_list = pandas_related.data_list(data)
data["Room Number"].to_list()


#create meeting room objects and populate in list of rooms
rooms = []

for i in room_list:
    #print(len(room_list))
    row = data[data["Room Number"]==i]
    room_info = MeetingroomInfo(row)
    rooms.append(room_info)

gui=TKGUI.Room_GUI()

window = Tk()
gui.gui_base(window)
#for i in rooms:
gui.add_room(rooms,window)
gui.update_button(rooms)
gui.ticket_button(rooms)

window.mainloop()


