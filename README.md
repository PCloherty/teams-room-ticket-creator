This project was a proof of concept to automate ticket creation in Kraftheinz for 20+ cookie cutter Teams room check tickets with different variations.

The requirements:
1: The automation should be flexible instead of set variables for room names and numbers due to potential changes in the London office or use in other offices.
  To achieve this I went with importing a CSV file as the default information on room names and numbers using Pandas.

2: It needs to have a GUI in order to change variables on if the hardware for the room is working or not.
  Using Pythons built-in TKinter to build the GUI in order to avoid potential library blocks from corporat security concern.  

3: Needs to interface with a web browser html elements as our ticket sysem is web based.
  To achieve this I used Selenium 4 with edge web driver as the corporate group policy uses edge as default.

4: The automation should record any changes to the default values by exporting another CSV file with the changes.
  Used Pandas to create the new dataframes after edits and exporting them to CSV files with the date of exportation.

The current bugs:
1: TKinter text widget does not have a variable method and so im unable to export the information typed into the notes text boxes.

2: This is being developped on a dedicated dev system outside of the Corporate enviroment in order to prevent possible security concerns of rogue code,
because of this ive had to simulate the ticket web page with test.HTML

3: Adding the full 20+ meeting rooms into the CSV will make the interface increase in length and some of the interface will be off the screen,
to fix this I need to make it pages/batches of a fixed number of rooms per page/batch
