from datetime import datetime

class Event:
    def __init__(self, event_name, date, user_id):
        self.event_name = event_name
        self.date = datetime.strptime(date, "%m/%d/%Y")
        self.user_id = user_id

    def to_message(self, date):
        date_to_use = date
        if date is None:
            date_to_use = datetime.now()

        relation = ""
        event_name = ""
        match self.event_name:
            case "Marriage":
                relation = ""
                event_name = "anniversary"
            case "Boy":
                relation = "son's "
                event_name = "birthday"
            case "Girl":
                relation = "daughter's "
                event_name = "birthday"

        msg = f"Everyone congratulate <@{self.user_id}> on his {relation}{self.get_years_since_ordinal(date_to_use)} {event_name}!"

        return msg

    def get_years_since_ordinal(self, date):
        date_to_use = date
        if date is None:
            date_to_use = datetime.now()

        years = date_to_use.year - self.date.year

        # from https://stackoverflow.com/a/20007730
        if 11 <= (years % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(years % 10, 4)]
        return str(years) + suffix


    @staticmethod
    def from_list(events):
        event_list = []
        for e in events:
            event_list.append(Event(e[0], e[1], e[2]))

        return event_list

    def __repr__(self):
        return f"{self.date}: {self.user_id} {self.event_name}"

