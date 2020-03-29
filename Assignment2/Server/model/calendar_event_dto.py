from model.calendar_event import CalendarEvent


class CalendarEventDTO:
    def __init__(self, name, description, scheduled_time):
        self.name = name
        self.description = description
        self.scheduled_time = scheduled_time

    @staticmethod
    def from_calendar_event(calendar_event):
        if calendar_event:
            return CalendarEventDTO(
                name=calendar_event.name,
                description=calendar_event.description,
                scheduled_time=calendar_event.scheduled_time)

    @staticmethod
    def to_calendar_event(calendar_event_dto):
        return CalendarEvent(
            name=calendar_event_dto.name,
            description=calendar_event_dto.description,
            scheduled_time=calendar_event_dto.scheduled_time)

    def __repr__(self):
        return "<CalendarEventDTO(name='%s', description='%s', scheduled_time='%s')>" % (
            self.name, self.description, str(self.scheduled_time))
