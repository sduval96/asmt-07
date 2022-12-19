import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass

# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
      
    def __init__(self,name, date):
        self.name = name
        self.date = date
        
    def get_name(self):
        return self.name
    
    def get_date(self):
        return self.date
    
    def __str__ (self):
        return f'{self.name} ({self.date})'
        # Holiday output when printed.
        
    def __eq__(self, other):
        try:
            return self.name == other.get_name()
        except:
            False
            
class HolidayList(Holiday):
    def __init__(self):
        self.innerHolidays = []
        
    def addHoliday(self, holidayObj):
        if not isinstance(holidayObj, Holiday):
            raise TypeError("holidayObj data type incorrect")
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        self.innerHolidays.append(holidayObj)
        # print to the user that you added a holiday
        

    def findHoliday(self, HolidayName, Date):
        findHoliday = Holiday(HolidayName, Date)
        for i in self.innerHolidays:
            if i == findHoliday:
                return i
        return False
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(self, HolidayName, Date):
        removeHoliday = self.findHoliday(HolidayName, Date)
        if removeHoliday == False:
            return False
        else:
            self.innerHolidays.remove(removeHoliday)
            print("Holiday removed")
            
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json(self, filelocation):
        # Read in things from json file location
        with open('holidays.json', "r") as f:
            data = json.load(f)
            for i in data['holidays']:
                holiday = i['name']
                date = i['date']
                date = date.split("-")
                date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                # Use addHoliday function to add holidays to inner list.
                self.addHoliday(Holiday(holiday, date))

    def save_to_json(self, filelocation):
        with open('holidays_updated.json', 'w') as f:
            for i in self.innerHolidays:
                json.dump({'name': i.get_name(), 'date': str(i.get_date())}, f, indent=4) # need to add get_name and get_date
            
        # Write out json file to selected file.
        
    def scrapeHolidays():
        import requests
        from bs4 import BeautifulSoup
        url = 'https://www.timeanddate.com/holidays/us/2018'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        new_holidays = [[td.text.strip() for td in tr.select('th, td')] for tr in soup.select('tr[data-mask]')]
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays(self):
        return len(self.innerHolidays)
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(year, week_number):
        year, week_number = int(year), int(week_number)
        holidays = (lambda holiday: (holiday.get_week() == week_number and holiday.get_year() == year), self.innerHolidays)
        holidays = list(filter(holidays))
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        return holidays

        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def displayHolidaysInWeek(holidayList):
        pass
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        pass
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek():
        pass
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        
    def add_holiday_helper(holidayList):
        print("Add a Holiday")
        HolidayName = input("Enter a holiday: ")
        Date = input('Enter a date (yyyy-mm-dd): ')
        Date = Date.split('-')
        while type(Date) != datetime.date:
            try:
                Date = datetime.date(int(Date[0]), int(Date[1]), int(Date[2]))
            except:
                print("Oops... that wasn't a valid date. Try that one more time.")
                Date = input('Enter a date (yyyy-mm-dd): ')
                Date = Date.split('-')

        holidayObj = Holiday(HolidayName, Date)
        holidayList.addHoliday(holidayObj)
        print("Congrats on your new Holiday")

    def remove_holiday_helper(holidayList):
        print("Remove a Holiday...")
        HolidayName = input("Please enter the name of the Holiday you would like to remove: ")
        Date = input('Enter a date (yyyy-mm-dd): ')
        Date = Date.split('-')
        while type(Date) != datetime.date:
            try:
                Date = datetime.date(int(Date[0]), int(Date[1]), int(Date[2]))
            except:
                print("Oops... that wasn't a valid date. Try that one more time")
                Date = input('Enter a date (yyyy-mm-dd): ')
                Date = Date.split('-')

        holidayObj = Holiday(HolidayName, Date)
        holidayList.removeHoliday(HolidayName, Date)


    def save_holiday_helper(holidayList):
        print("Saving Holiday List...")
        print("======================")
        prompt = input("Are you sure you want to save your file. Enter y/n: ")
        print("")
        if prompt == 'y':
            holidayList.save_to_json('holidays_updated.json')
            print("Success:")
            print("You have saved your changes \n")
        elif prompt == 'n':
            print("Canceled:")
            print("Save canceled \n")
        else:
            print("That is an incorrect response: Try again")
        
def main():
    holidayList = HolidayList()
    holidayList.read_json('holidays.json')
    
    print("Holiday Management")
    print("==================")
    print(f'There are {holidayList.numHolidays()} holidays stored in the system. \n')

    holiday_menu = ["Add a Holiday", "Remove a Holiday", "Save Holiday List", "View Holidays", "Exit"]
    
    stillinMenu = True
    while stillinMenu:
        print('Holiday Menu')
        print('============')
        for i in range(len(holiday_menu)):
            print(f'{i + 1}. {holiday_menu[i]}')
            choice = 'n'

        menu_choice = int(input("Please enter the number for the menu option: "))
        if menu_choice == 1:
            add_holiday_helper(holidayList)
        elif menu_choice == 2:
            remove_holiday_helper(holidayList)
        elif menu_choice == 3:
            save_holiday_helper(holidayList)
        elif menu_choice == 4:
            displayHolidaysInWeek()
        elif menu_choice == 5:
            print("")
            print("Exit")
            print("====")
            exit_choice = input("Are you sure you want to exit? y/n: ")
            if exit_choice == 'y':
                print("Goodbye: Enjoy your holiday party.")
                stillinMenu = False
            else:
                print("")
                print("Returning you to the main menu... \n")
        else:
            continue
main()
        
    
            







