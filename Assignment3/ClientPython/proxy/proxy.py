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
        return list(map(CalendarEventDTO.fromDict, self.proxy.events_list()))

    def events_list_by_name(self, name):
        return list(map(CalendarEventDTO.fromDict, self.proxy.events_list_by_name(name)))

    def events_list_by_description(self, description):
        return list(map(CalendarEventDTO.fromDict, self.proxy.events_list_by_description(description)))

    def event_add(self, name, description, scheduled_time):
        return self.proxy.event_add(name, description, scheduled_time)

    def event_edit(self, original_name, updated_name, updated_description, updated_scheduled_time):
        return self.proxy.event_edit(original_name, updated_name, updated_description, updated_scheduled_time)

    def event_delete(self, name):
        return self.proxy.event_delete(name)
