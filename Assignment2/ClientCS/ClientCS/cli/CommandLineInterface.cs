using ClientCS.model;
using EasyConsole;
using Razorvine.Pyro;
using System;
using System.Collections.Generic;

namespace ClientCS.cli
{
    class CommandLineInterface
    {
        private readonly PyroProxy proxy;
        private readonly string dateTimeFormatter = "yyyy'-'MM'-'dd HH':'mm':'ss";

        public CommandLineInterface(PyroProxy proxy)
        {
            this.proxy = proxy;
        }

        public void HandleCliStart()
        {
            Menu mainOptionsMenu = new Menu();

            mainOptionsMenu.Add(MenuOptions.LIST_ALL_EVENTS, HandleListAllEvents);
            mainOptionsMenu.Add(MenuOptions.SEARCH_EVENT_BY_NAME, HandleListEventsByName);
            mainOptionsMenu.Add(MenuOptions.SEARCH_EVENTS_BY_DESCRIPTION, HandleListEventsByDescription);
            mainOptionsMenu.Add(MenuOptions.CREATE_EVENT, HandleCreateEvent);
            mainOptionsMenu.Add(MenuOptions.QUIT, () => Environment.Exit(0));

            mainOptionsMenu.Display();
        }

        private void HandleListAllEvents()
        {
            List<object> eventsObjects = (List<object>)proxy.call("events_list");

            List<CalendarEventDto> events = eventsObjects.ConvertAll(new Converter<object, CalendarEventDto>(CalendarEventDto.CalendarEventDtoFromDict));

            HandleDisplayEventList(events);
        }

        private void HandleListEventsByName()
        {
            string name = Input.ReadString("Name:");

            List<object> eventsobjects = (List<object>)proxy.call("events_list_by_name", name);

            List<CalendarEventDto> events = eventsobjects.ConvertAll(new Converter<object, CalendarEventDto>(CalendarEventDto.CalendarEventDtoFromDict));

            HandleDisplayEventList(events);
        }

        private void HandleListEventsByDescription()
        {
            string description = Input.ReadString("Description:");

            List<object> eventsobjects = (List<object>)proxy.call("events_list_by_description", description);

            List<CalendarEventDto> events = eventsobjects.ConvertAll(new Converter<object, CalendarEventDto>(CalendarEventDto.CalendarEventDtoFromDict));

            HandleDisplayEventList(events);
        }

        private void HandleCreateEvent()
        {
            string name = Input.ReadString("Name:");
            string description = Input.ReadString("Description:");
            string scheduled_time = Input.ReadString("Date and time (YYYY-MM-ZZ HH:MM:SS)");

            proxy.call("event_add", name, description, scheduled_time);

            HandleListAllEvents();
        }

        private void HandleDisplayEventList(List<CalendarEventDto> events)
        {
            Menu eventSelectionMenu = new Menu();

            for (int i = 0; i < events.Count; i++)
            {
                CalendarEventDto selectedEvent = events[i];
                eventSelectionMenu.Add(
                   new Option(selectedEvent.name + " | " + selectedEvent.scheduled_time.ToString(dateTimeFormatter),
                   () => HandleEventSelection(selectedEvent))
                );
            }

            eventSelectionMenu.Add("Back", HandleCliStart);

            eventSelectionMenu.Display();
        }

        private void HandleEventSelection(CalendarEventDto calendarEventDto)
        {
            Console.WriteLine(calendarEventDto.name + " | " + calendarEventDto.scheduled_time.ToString(dateTimeFormatter));
            Console.WriteLine(calendarEventDto.description);

            Menu eventOperationsMenu = new Menu();

            eventOperationsMenu.Add(EventOperationOptions.EDIT, () => HandleEventEdit(calendarEventDto));
            eventOperationsMenu.Add(EventOperationOptions.DELETE, () => HandleEventDelete(calendarEventDto));
            eventOperationsMenu.Add(EventOperationOptions.BACK, HandleListAllEvents);

            eventOperationsMenu.Display();
        }

        private void HandleEventEdit(CalendarEventDto calendarEventDto)
        {
            string name = Input.ReadString("Name [" + calendarEventDto.name + "]:");
            string description = Input.ReadString("Description [" + calendarEventDto.description + "]:");
            string scheduled_time = Input.ReadString("Date and time [" + calendarEventDto.scheduled_time.ToString(dateTimeFormatter) + "]:");

            string updatedName = name != null && name != "" ? name : calendarEventDto.name;
            string updatedDescription = description != null && description != "" ? description : calendarEventDto.description;
            string updatedScheduledTime = scheduled_time != null && scheduled_time != "" ? scheduled_time : calendarEventDto.scheduled_time.ToString(dateTimeFormatter);

            proxy.call("event_edit", calendarEventDto.name, updatedName, updatedDescription, updatedScheduledTime);

            HandleListAllEvents();
        }


        private void HandleEventDelete(CalendarEventDto calendarEventDto)
        {
            proxy.call("event_delete", calendarEventDto.name);

            HandleListAllEvents();
        }
    }
}
