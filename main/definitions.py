import datetime


def get_formatted_date(date):
    DATE_FORMAT = "%A, %m/%d/%Y"
    return date.strftime(DATE_FORMAT)


class Person
    is_open = False
    next_touch = None
    to_do = None
    contacts = []

    def __init__(self, name, referrers, companies, position):
        self.name = name
        self.referrers = referrers
        self.companies = companies
        self.position = position

    def __repr__(self):
        if not self.contacts
            return self.name + "\nNO CONTACT MADE"

        if is_open:
            return self.name +
                   ":\ncompanies: " + self.companies +
                   "\nlast contact: " + self.contacts[-1]
        return self.name +
               ":\nCLOSED ON " + get_formatted_date(self.contacts[-1].last_touch) +
               "notes:\n" + self.contacts[-1].notes

    def add_contact(self, contact):
        self.is_open = contact.is_open
        if contact.is_open:
            self.next_touch = contact.next_touch
            self.to_do = contact.to_do
        else:
            self.next_touch = None
            self.to_do = None
        self.contacts.append(contact)

class Contact
    STALE_TIME = 7  # Days until contact is considered stale
    def __init__(self, next_touch, status, is_open, notes, to_dos, last_touch, next_touch):
        self.last_touch = last_touch or datetime.date.today()
        self.next_touch = next_touch or self.last_touch + datetime.timedelta(days=self.STALE_TIME)
        self.status = status
        self.is_open = is_open
        self.notes = notes
        self.to_do = to_do

    def __repr__(self):
        return self.status +
               "\nlast touch: " + get_formatted_date(self.last_touch) +
               "\nnext touch: " + get_formatted_date(self.next_touch) + 
               "\nACTIONABLE: " + to_do
