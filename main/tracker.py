import datetime
from main.definitions import Person, Contact, get_formatted_date



def run():
    all_people = []

    def load_activities():  # TODO implement
        # load people from text file
        return []

    def get_main_options():  # TODO implement
        # return all main menu options
        return "Do Something\nHelp\nExit"

    def get_date_actionables(date):
        actionable = []
        for person in all_people:
            if person.next_touch and person.is_open and person.next_date <= date:
                actionable.append(person)
        return actionable

    def get_todays_actionables():
        return get_date(datetime.date.today())


    def get_dates_actionables(date_start, date_end):
        actionable_dates = {}
        if date_end > date_start:
            cur_date = date_start
            while cur_date <= date_end:
                actionable_dates[get_formatted_date(cur_date)] = get_date_actionables(cur_date)

        return actionable_dates

    print "loading all activities"
    all_people = load_activities()
    print "activities loaded"

    print "Welcome to the Activity Tracker."
    while True:  # Feedback loop
        # Continue to go back to main menu
        # Break to exit
        print "Main Menu:"
        print get_main_options()

    # User Requested an Exit (or something broke terribly)
    print "Save changes?"
    # User input

    print "Goodbye"
