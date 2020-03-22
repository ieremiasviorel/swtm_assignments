import sys

import Pyro4

Pyro4.config.SERIALIZERS_ACCEPTED = {'json', 'marshal', 'serpent', 'pickle'}
Pyro4.config.SERIALIZER = 'pickle'


class ExecPyro4Clie:
    def __init__(self, urlServ):
        proxy = Pyro4.Proxy(urlServ)
        print("Client Python Pyro4: " + urlServ)
        print("ping: \t" + proxy.ping())
        print("upcase: \tnegru = " + proxy.upcase("negru"))
        print("add: \t66 + 75 = " + str(proxy.add(66, 75)))
        print("ping: \t" + proxy.ping())
        print("event: \t" + str(proxy.event().name))


if len(sys.argv) > 1:
    ExecPyro4Clie(sys.argv[1])
else:
    ExecPyro4Clie("PYRO:exec@localhost:7543")
