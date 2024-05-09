import pandas
from datetime import date

def read_data():
    data = pandas.read_csv("test3.csv")
    return data

def data_list(data):
    room_list = data["Room Number"].to_list()
    return room_list

def create_frame(data):
        df = []
        for i in data:
            df.append({
                "Room Number":i.room_number,
                "Room Name":i.room_name,
                "Microphone":i.microphone,
                "Camera":i.camera,
                "Speakers":i.speakers,
                "Display":i.display,
                "Booking":i.booking_panel 
                })
        return df
                
def write_data(list_of_dict):
    df=pandas.DataFrame(list_of_dict)
    df.to_csv("Meetingroom_Check "+str(date.today())+".csv", index=False)

    



