import sys
import xmlrpc.client

import Uri


class Xy1Clie:
    def __init__(self, urlServ):
        print("Client Python XML-RPC "+urlServ)
        uri = Uri.uriFields(urlServ)
        pathServ = uri["path"]
        if pathServ.endswith(".php"):
            pathServ = ""
            proxy = xmlrpc.client.ServerProxy(
                "http://"+uri["host"]+":"+uri["port"]+"/"+uri["path"])
        else:
            pathServ += "."
            proxy = xmlrpc.client.ServerProxy(
                "http://"+uri["host"]+":"+uri["port"])

        # print ("ping: \t"+proxy.Xy1.ping()) # apel static
        print("ping: \t"+getattr(proxy, pathServ+"ping")())  # apel dinamic
        print("upcase: \tnegru = "+getattr(proxy, pathServ+"upcase")("negru"))
        print("add: \t66 + 75 = "+str(getattr(proxy, pathServ+"add")(66, 75)))
        print("events_list: \t" + str(getattr(proxy, pathServ+"events_list")()))


if len(sys.argv) > 1:
    Xy1Clie(sys.argv[1])
else:
    Xy1Clie("http://localhost/Xh1Serv.php")
