from tkinter import *
import pandas_related
import Selenium_related

RADIO_VAR={"microphone_var":[], 
           "camera_var":[],
            "display_var":[],
            "speakers_var":[],
            "touch_var":[],
            "notes_var": []}
class Room_GUI:
    def __init__(self):
        self.row=0
        
    def gui_base(self,window):
        window.config(width=700,height=500)
        window.title("Meeting Streamline")

        # Title layout
        r_num_t_label=Label(text="Room Number")
        r_num_t_label.grid(column=0, row=self.row)
        r_nam_t_label=Label(text="Room Name")
        r_nam_t_label.grid(column=1, row=self.row)

        microphone_t_label=Label(text="Microphone")
        microphone_t_label.grid(column=2, row=self.row)
        camera_t_label=Label(text="Camera")
        camera_t_label.grid(column=3, row=self.row)

        speaker_t_label=Label(text="Speaker")
        speaker_t_label.grid(column=4, row=self.row)
        display_t_label=Label(text="Display")
        display_t_label.grid(column=5, row=self.row)

        Booking_t_label=Label(text="Booking panel")
        Booking_t_label.grid(column=6, row=self.row)
        notes_t_label=Label(text="Notes")
        notes_t_label.grid(column=7, row=self.row) 

        self.row+=1   
    
    def add_room(self,rooms,window):
        
        for idx, room_object in enumerate(rooms):

            #set defaultradio values
            RADIO_VAR["microphone_var"].append(StringVar(value=rooms[idx].microphone))
            RADIO_VAR["camera_var"].append(StringVar(value=rooms[idx].camera))
            RADIO_VAR["display_var"].append(StringVar(value=rooms[idx].display))
            RADIO_VAR["speakers_var"].append(StringVar(value=rooms[idx].speakers))
            RADIO_VAR["touch_var"].append(StringVar(value=rooms[idx].booking_panel))
            RADIO_VAR["notes_var"].append(rooms[idx].notes)
            
            #number and name labels
            Label(text=room_object.room_number).grid(column=0, row=self.row,rowspan=2)
            Label(text=room_object.room_name).grid(column=1, row=self.row,rowspan=2)

            # microphone radio            
            microphone_y_radio = Radiobutton(window, text="Yes",variable=RADIO_VAR["microphone_var"][idx],value="Yes")
            microphone_y_radio.grid(row=self.row, column=2)
            microphone_n_radio = Radiobutton(window, text="No",variable=RADIO_VAR["microphone_var"][idx],value="No")
            microphone_n_radio.grid(row=self.row+1, column=2)
            
            # Camera radios            
            camera_y_radio=Radiobutton(window,text="Yes", variable=RADIO_VAR["camera_var"][idx], value="Yes")
            camera_y_radio.grid(column=3,row=self.row,rowspan=1)
            camera_n_radio=Radiobutton(window,text="No", variable=RADIO_VAR["camera_var"][idx], value="No")
            camera_n_radio.grid(column=3,row=self.row+1,rowspan=1)

            # Speaker Radio
            speaker_y_radio=Radiobutton(text="Yes", variable=RADIO_VAR["speakers_var"][idx], value="Yes")
            speaker_y_radio.grid(column=4,row=self.row,rowspan=1)
            speaker_n_radio=Radiobutton(text="No", variable=RADIO_VAR["speakers_var"][idx], value="No")
            speaker_n_radio.grid(column=4,row=self.row+1,rowspan=1)

            # Display radio           
            display_y_radio=Radiobutton(text="Yes", variable=RADIO_VAR["display_var"][idx], value="Yes")
            display_y_radio.grid(column=5,row=self.row,rowspan=1)
            display_n_radio=Radiobutton(text="No", variable=RADIO_VAR["display_var"][idx], value="No")
            display_n_radio.grid(column=5,row=self.row+1,rowspan=1)
        
            # Booking panel            
            booking_y_radio=Radiobutton(text="Yes", variable=RADIO_VAR["touch_var"][idx], value="Yes")
            booking_y_radio.grid(column=6,row=self.row,rowspan=1)
            booking_n_radio=Radiobutton(text="No", variable=RADIO_VAR["touch_var"][idx], value="No")
            booking_n_radio.grid(column=6,row=self.row+1,rowspan=1)
        
            # notes
            notes_text=Text(height=5,width=30)
            notes_text.grid(column=7,row=self.row, rowspan=2)
            self.row+=2
            
    def update_att(self,rooms, radios):
        for ind in enumerate(rooms):
           # print(rooms)
            rooms[ind[0]].microphone = radios['microphone_var'][ind[0]].get()
            rooms[ind[0]].camera = radios['camera_var'][ind[0]].get()
            rooms[ind[0]].speakers = radios['speakers_var'][ind[0]].get()
            rooms[ind[0]].display = radios['display_var'][ind[0]].get()
            rooms[ind[0]].booking_panel = radios['touch_var'][ind[0]].get()

        new_data=pandas_related.create_frame(rooms)
        pandas_related.write_data(new_data)
        
    def update_button(self,rooms):
        update_button = Button(text="Update",bg="#C8C3C2", command=lambda : self.update_att(rooms,RADIO_VAR))
        update_button.grid(column=5,row=self.row+1)
        
    def make_tickets(self,rooms):
        sel = Selenium_related
        for i in  enumerate(rooms):
            name= rooms[i[0]].room_name
            number = rooms[i[0]].room_number
            sel.bridge(number, name)

    def ticket_button(self, rooms):
        #print(rooms)
        update_button = Button(text="Make Tickets",bg="#C8C3C2", command=lambda : self.make_tickets(rooms))
        update_button.grid(column=6,row=self.row+1)
