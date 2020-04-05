from model.calendar_event import CalendarEvent
from model.calendar_event_dto import CalendarEventDTO


class CalendarEventService:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def persist(self, calendar_event_dto):
        return CalendarEvent.persist(self.session_factory(), CalendarEventDTO.to_calendar_event(calendar_event_dto))

    def delete(self, calendar_event_dto_name):
        calendar_event = CalendarEvent.get_by_name(self.session_factory(), calendar_event_dto_name)
        return CalendarEvent.delete(self.session_factory(), calendar_event)

    def update(self, current_event_name, updated_calendar_event_dto):
        current_calendar_event = CalendarEvent.get_by_name(self.session_factory(), current_event_name)
        updated_calendar_event = self.update_event_fields(current_calendar_event, updated_calendar_event_dto)
        return CalendarEvent.persist(self.session_factory(), updated_calendar_event)

    def get_all(self):
        return self.convert_to_dto(CalendarEvent.get_all(self.session_factory()))

    def get_by_name(self, event_name):
        return CalendarEventDTO.from_calendar_event(CalendarEvent.get_by_name(self.session_factory(), event_name))

    def get_by_description_partial(self, event_description):
        return self.convert_to_dto(CalendarEvent.get_by_description_partial(self.session_factory(), event_description))

    def convert_to_dto(self, calendar_events):
        return list(map(CalendarEventDTO.from_calendar_event, calendar_events))

    def update_event_fields(self, current_calendar_event, updated_calendar_event_dto):
        current_calendar_event.name = updated_calendar_event_dto.name
        current_calendar_event.description = updated_calendar_event_dto.description
        current_calendar_event.scheduled_time = updated_calendar_event_dto.scheduled_time

        return current_calendar_event
