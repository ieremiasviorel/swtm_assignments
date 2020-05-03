import socket
from datetime import datetime

import Pyro4
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from model.calendar_event_dto import CalendarEventDTO
from service.calendar_event_service import CalendarEventService

Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')


@Pyro4.expose
class ExecPyro4Serv(object):
    def __init__(self, calendar_event_service):
        self.calendar_event_service = calendar_event_service

    def ping(self):
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        return "Python ExecPyro4" + ": " + name + "(" + ip + ":7543" + "), " + str(datetime.now())

    def upcase(self, s):
        return s.upper()

    def add(self, a, b):
        return a + b

    def events_list(self):
        return self.calendar_event_service.get_all()

    def events_list_by_name(self, name):
        return self.calendar_event_service.get_by_name_partial(name)

    def events_list_by_description(self, description):
        return self.calendar_event_service.get_by_description_partial(description)

    def event_add(self, event_name, event_description, event_scheduled_time):
        calendar_event_dto = CalendarEventDTO(event_name, event_description, event_scheduled_time)
        return self.calendar_event_service.persist(calendar_event_dto)

    def event_edit(self, original_event_name, updated_event_name, updated_event_description,
                   updated_event_scheduled_time):
        updated_calendar_event_dto = CalendarEventDTO(updated_event_name, updated_event_description,
                                                      updated_event_scheduled_time)
        return self.calendar_event_service.update(original_event_name, updated_calendar_event_dto)

    def event_delete(self, event_name):
        return self.calendar_event_service.delete(event_name)


def init_database():
    return sqlalchemy.create_engine('mysql://root:root@localhost:3306/wsmt_assig2_pyro')


def init_database_session_factory(engine):
    return sessionmaker(bind=engine)


def start_server(calendar_event_service):
    daemon = Pyro4.Daemon(port=7543)
    uri = daemon.register(ExecPyro4Serv(calendar_event_service), "exec")
    print("Python ExecPyro4 waiting at: " + str(uri))
    daemon.requestLoop()


if __name__ == "__main__":
    engine = init_database()

    sessionFactory = init_database_session_factory(engine)

    calendar_event_service = CalendarEventService(sessionFactory)

    start_server(calendar_event_service)
