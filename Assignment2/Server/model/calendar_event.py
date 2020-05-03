from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CalendarEvent(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    scheduled_time = Column(DateTime(), nullable=False)

    def __repr__(self):
        return "<CalendarEvent(name='%s', description='%s', scheduled_time='%s')>" % (
            self.name, self.description, str(self.scheduled_time))

    @staticmethod
    def persist(session, event):
        session.add(event)
        session.commit()

    @staticmethod
    def delete(session, event):
        session.delete(event)
        session.commit()

    @staticmethod
    def get_all(session):
        events = session.query(CalendarEvent) \
            .order_by(CalendarEvent.scheduled_time.asc()) \
            .all()
        session.close()
        return events

    @staticmethod
    def get_by_name(session, event_name):
        event = session.query(CalendarEvent).filter_by(name=event_name).first()
        session.close()
        return event

    @staticmethod
    def get_by_name_partial(session, event_name):
        events = session.query(CalendarEvent) \
            .filter(CalendarEvent.name.contains(event_name)) \
            .order_by(CalendarEvent.scheduled_time.asc()) \
            .all()
        session.close()
        return events

    @staticmethod
    def get_by_description_partial(session, event_description):
        events = session.query(CalendarEvent) \
            .filter(CalendarEvent.description.contains(event_description)) \
            .order_by(CalendarEvent.scheduled_time.asc()) \
            .all()
        session.close()
        return events
