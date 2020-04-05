package com.swtm.pyro.assig.cli;

import com.swtm.pyro.assig.model.CalendarEventDto;
import net.razorvine.pyro.PyroProxy;
import org.beryx.textio.TextIO;
import org.beryx.textio.TextTerminal;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CommandLineInterface {
    private final DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ISO_LOCAL_DATE_TIME;

    private PyroProxy proxy;
    private TextIO textInterface;
    private TextTerminal textTerminal;

    public CommandLineInterface(PyroProxy proxy, TextIO textInterface, TextTerminal textTerminal) {
        this.proxy = proxy;
        this.textInterface = textInterface;
        this.textTerminal = textTerminal;
    }

    public void handleCliStart() throws IOException {
        showMenuOptions();
    }

    private void showMenuOptions() throws IOException {
        MenuOptions menuOption = this.textInterface.newEnumInputReader(MenuOptions.class).read("Select an option:");
        handleMenuOptionsSelection(menuOption);
    }

    private void handleMenuOptionsSelection(MenuOptions menuOption) throws IOException {
        switch (menuOption) {
            case LIST_ALL_EVENTS: {
                List<Map<String, String>> eventsStr = (List<Map<String, String>>) proxy.call("events_list");
                List<CalendarEventDto> events = eventsStr.stream().map(CalendarEventDto::new).collect(Collectors.toList());
                this.showEventsList(events);
                break;
            }
            case SEARCH_EVENT_BY_NAME: {
                String eventName = this.textInterface.newStringInputReader().withPattern("^[a-zA-Z0-9-_ ]+$").read("Name");
                Map<String, String> eventStr = (Map<String, String>) proxy.call("event_find_by_name", eventName);
                if (eventStr != null) {
                    CalendarEventDto event = new CalendarEventDto(eventStr);
                    this.showEventsList(Arrays.asList(event));
                } else {
                    this.showEventsList(new ArrayList<>());
                }
                break;
            }
            case SEARCH_EVENTS_BY_DESCRIPTION: {
                String eventDescription = this.textInterface.newStringInputReader().read("Description");
                List<Map<String, String>> eventsStr = (List<Map<String, String>>) proxy.call("events_list_by_description", eventDescription);
                List<CalendarEventDto> events = eventsStr.stream().map(CalendarEventDto::new).collect(Collectors.toList());
                this.showEventsList(events);
                break;
            }
            case CREATE_EVENT: {
                this.handleEventCreation();
                break;
            }
            case QUIT: {
                System.exit(0);
            }
        }
    }

    private void showEventsList(List<CalendarEventDto> events) throws IOException {
        int i = 1;
        for (CalendarEventDto event : events) {
            this.textTerminal.printf("%d. %s | %s\n", i, event.getName(), this.formatDateTimeForDisplay(event.getScheduled_time()));
            i++;
        }
        this.textTerminal.printf("%d. Back\n", i);

        int eventIndex = this.textInterface.newIntInputReader()
                .withMinVal(1)
                .withMaxVal(events.size() + 1)
                .read("Select an option:");

        if (eventIndex == events.size() + 1) {
            this.showMenuOptions();
        } else {
            CalendarEventDto selectedEvent = events.get(eventIndex - 1);
            handleEventSelection(selectedEvent);
        }
    }

    private void handleEventSelection(CalendarEventDto event) throws IOException {
        this.textTerminal.printf("Name: %s | Scheduled time: %s\n", event.getName(), this.formatDateTimeForDisplay(event.getScheduled_time()));
        this.textTerminal.println("Description: " + event.getDescription());

        handleEventOperationSelection(event);
    }


    private void handleEventOperationSelection(CalendarEventDto event) throws IOException {
        EventOperationOptions eventOperationOption = this.textInterface.newEnumInputReader(EventOperationOptions.class)
                .read("Select an option:");

        switch (eventOperationOption) {
            case EDIT: {
                String updatedEventName = this.textInterface.newStringInputReader()
                        .withDefaultValue(event.getName())
                        .withPattern("^[a-zA-Z0-9-_ ]+$")
                        .read("Name");
                String updatedEventDescription = this.textInterface.newStringInputReader()
                        .withDefaultValue(event.getDescription())
                        .read("Description");
                String updatedEventScheduledTime = this.textInterface.newStringInputReader()
                        .withDefaultValue(this.formatDateTimeForDisplay(event.getScheduled_time()))
                        .withPattern("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$")
                        .read("Date and time (YYYY-MM-ZZ HH:MM:SS)");

                this.proxy.call("event_edit", event.getName(), updatedEventName, updatedEventDescription, updatedEventScheduledTime);
                this.handleMenuOptionsSelection(MenuOptions.LIST_ALL_EVENTS);
                break;
            }
            case DELETE: {
                this.proxy.call("event_delete", event.getName());
                this.handleMenuOptionsSelection(MenuOptions.LIST_ALL_EVENTS);
                break;
            }
            case BACK: {
                this.handleMenuOptionsSelection(MenuOptions.LIST_ALL_EVENTS);
                break;
            }
        }
    }

    private void handleEventCreation() throws IOException {
        String eventName = this.textInterface.newStringInputReader().withPattern("^[a-zA-Z0-9-_ ]+$").read("Name");
        String eventDescription = this.textInterface.newStringInputReader().read("Description");
        String eventScheduledTime = this.textInterface.newStringInputReader()
                .withPattern("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$")
                .read("Date and time (YYYY-MM-ZZ HH:MM:SS)");

        this.proxy.call("event_add", eventName, eventDescription, eventScheduledTime);
        this.handleMenuOptionsSelection(MenuOptions.LIST_ALL_EVENTS);
    }

    private String formatDateTimeForDisplay(LocalDateTime dateTime) {
        return this.dateTimeFormatter.format(dateTime).replace("T", " ");
    }
}
