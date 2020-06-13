import xmlrpc.client
import Uri
from model.calendar_event_dto import CalendarEventDTO


class Proxy:
    def __init__(self, urlServ):
        uri = Uri.uriFields(urlServ)
        pathServ = uri["path"]
        if pathServ.endswith(".php"):
            pathServ = ""
            self.proxy = xmlrpc.client.ServerProxy(
                "http://" + uri["host"] + ":" + uri["port"] + "/" + uri["path"])
        else:
            pathServ += "."
            self.proxy = xmlrpc.client.ServerProxy(
                "http://" + uri["host"] + ":" + uri["port"])

    def events_list(self):
        return map(CalendarEventDTO.fromDict, self.proxy.events_list())
