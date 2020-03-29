class CalendarEventDTO:
    def __init__(self, name, description, scheduled_time):
        self.name = name
        self.description = description
        self.scheduled_time = scheduled_time

    def __repr__(self):
        return "<CalendarEventDTO(name='%s', description='%s', scheduled_time='%s')>" % (
            self.name, self.description, str(self.scheduled_time))
