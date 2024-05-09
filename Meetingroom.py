class MeetingroomInfo:
    def __init__(self,meetingroom):
        self.room_number = meetingroom["Room Number"].item()
        self.room_name = meetingroom["Room Name"].item()
        self.microphone= meetingroom["Microphone"].item()
        self.camera=meetingroom["Camera"].item()
        self.speakers=meetingroom["Speakers"].item()
        self.display=meetingroom["Display"].item()
        self.booking_panel=meetingroom["Booking Panel"].item()
        self.notes=meetingroom["Notes"].item()
        
        

    def update_room(self, meetingroom):
        self.room_number = meetingroom["Room Number"].item()
        self.room_name = meetingroom["Room Name"].item()
        self.microphone= meetingroom["Microphone"].item()
        self.camera=meetingroom["Camera"].item()
        self.speakers=meetingroom["Speakers"].item()
        self.display=meetingroom["Display"].item()
        self.booking_panel=meetingroom["Booking Panel"].item()
        self.notes=meetingroom["Notes"].item()
        self.rooms.append(self.room_number)
        #print(f"{self.__dict__}")
            
         
    
