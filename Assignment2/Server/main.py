import socket
from datetime import datetime

import Pyro4

from model.calendarEvent import CalendarEvent

Pyro4.config.SERIALIZERS_ACCEPTED = {'json', 'marshal', 'serpent', 'pickle'}
Pyro4.config.SERIALIZER = 'pickle'


@Pyro4.expose
class ExecPyro4Serv(object):
    def ping(self):
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        return "Python ExecPyro4" + ": " + name + "(" + ip + ":7543" + "), " + str(datetime.now())

    def upcase(self, s):
        return s.upper()

    def add(self, a, b):
        return a + b

    def event(self):
        return CalendarEvent('Default name', 'Default description', datetime.now())


def start():
    daemon = Pyro4.Daemon(port=7543)
    uri = daemon.register(ExecPyro4Serv(), "exec")
    print("Python ExecPyro4 waiting at: " + str(uri))
    daemon.requestLoop()


if __name__ == "__main__":
    start()
