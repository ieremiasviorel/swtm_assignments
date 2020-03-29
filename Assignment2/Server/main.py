import socket
from datetime import datetime

import Pyro4
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from service.calendar_event_service import CalendarEventService

Pyro4.config.SERIALIZERS_ACCEPTED = {'json', 'marshal', 'serpent', 'pickle'}
Pyro4.config.SERIALIZER = 'pickle'


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

    def event_find_by_name(self, name):
        return self.calendar_event_service.get_by_name(name)

    def events_list_by_description(self, description):
        return self.calendar_event_service.get_by_description_partial(description)

    def event_add(self, event):
        return self.calendar_event_service.persist(event)

    def event_edit(self, original_event_name, updated_event):
        return self.calendar_event_service.update(original_event_name, updated_event)

    def event_delete(self, event):
        return self.calendar_event_service.delete(event)


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
