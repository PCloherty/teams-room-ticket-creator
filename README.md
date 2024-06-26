Summery:
A python program created with Pandas and Selenium libraries (for data handling and web interaction for Snow access respectively) as a proof of concept on automating the ticket creation in larger offices with many rooms. 

The program is flexible with the room name and numbers as it gets all the information from Rooms.CSV file, which can be customized to represent the name and number of the rooms in EUC Local office.

As this was a project made as a proof of concept, I have had to make use of a placeholder webpage for the integration with Snow, however it uses the same HTML elements as the the companies SNow request creation page.  


The requirements:

1: The automation should be flexible instead of set variables for room names and numbers due to potential changes in the KH London office or use in other KH offices.
  To achieve this I went with importing a CSV file as the default information on room names and numbers using Pandas.

2: It needs to have a GUI in order to change variables on if the hardware for the room is working or not.
  Using Pythons built-in TKinter to build the GUI in order to avoid potential library blocks from corporat security concern.  

3: Needs to interface with a web browser html elements as our ticket sysem is web based.
  To achieve this I used Selenium 4 with edge web driver as the corporate group policy uses edge as default.

4: The automation should record any changes to the default values by exporting another CSV file with the changes.
  Used Pandas to create the new dataframes after edits and exporting them to CSV files with the date of exportation.


The CSV file:

In the CSV file the user can edit the number and name to represent the meeting rooms of their local office, below is an image of a test CSV using 3 London rooms.
All the status data is defaulted to yes as it is expected that all the equipment should be working.  
![image](https://github.com/PCloherty/teams-room-ticket-creator/assets/43047949/af9c2d31-a158-4a25-978f-c9b4c34b2be4)


The UI:

Below is a snip of the UI after the data has been pulled and made into a data set. If an issue has been found in one of the meeting rooms, the EUC just needs to click on the “No” radio button under the effected hardware. After all changes have been made click “Update” to export a dated CSV for record of the current meeting room check and “Make Tickets” to run the automated aspect of the code.  
![image](https://github.com/PCloherty/teams-room-ticket-creator/assets/43047949/22739b76-0fdc-4ea7-8c27-3f68655c0bc2)


How it works:

You run the program which will import the Rooms.CSV to create a dataset based on the local office information provided by the local EUC.

When the EUC has made changes to reflect any issues, they can click on “Update” to export the current UI records to a dated spreadsheet in the form of YYYY-MM-DD(see below)
![image](https://github.com/PCloherty/teams-room-ticket-creator/assets/43047949/ec93b885-7bac-4ff9-a460-79fa6a003d0d)

When the EUC clicks “Make Tickets”, the selenium-edge plug-in kicks in and opens edge and will run through each row of data from the CSV filling the relevant HTML fields with information provided by the dataset taken from the UI interaction.

![image](https://github.com/PCloherty/teams-room-ticket-creator/assets/43047949/0a75280f-3214-4a0b-9cdf-4291f267de43)


Current Bugs and potential resolutions:

Currently there are two major Bugs and a small Bug.
  1.TKInter which is used to make the UI, will not import the text held in the in the notes field.  
    
    Changing the widget used to hold this data to an input widget will limit it to a single line, however this will allow the         information to be used in the data for the CSV export and tickets.
  
  2.Showing large amounts of rooms on the UI in one page will cause the bottom of the UI to fall out of view.
    
    Implementing a page-by-page system with limited number of rooms per page will allow all rooms to be viewable and the “update”     and “Make Tickets” buttons in sight.
  
  3.currently the code defaults to my name and Shard for the Engineer and Location
    
    Adding and creating a check for a EUC.CSV, if there is no file called EUC.CSV then prompt the user with an input where they       will copy their name and location from SNow and paste into the input prompt, this will then save as a CSV for future uses.
