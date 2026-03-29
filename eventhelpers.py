from event import Event
from sheets import get_data


def get_sheet_as_events():
    return Event.from_list(get_data())

async def act_on_events_of_day(events, date, action):
    for e in events:
        if e.date.month == date.month and e.date.day == date.day:
            await action(e)

async def act_on_sheet_for_day(date, action):
    return await act_on_events_of_day(get_sheet_as_events(), date, action)
