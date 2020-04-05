package com.swtm.pyro.assig.model;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.Map;

public class CalendarEventDto implements Serializable {

    private String name;
    private String description;
    private LocalDateTime scheduled_time;

    public CalendarEventDto() {
    }

    public CalendarEventDto(String name, String description, LocalDateTime scheduled_time) {
        this.name = name;
        this.description = description;
        this.scheduled_time = scheduled_time;
    }

    public CalendarEventDto(Map<String, String> calendarEventDtoMap) {
        this(calendarEventDtoMap.get("name"), calendarEventDtoMap.get("description"), LocalDateTime.parse(calendarEventDtoMap.get("scheduled_time")));
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public LocalDateTime getScheduled_time() {
        return scheduled_time;
    }

    public void setScheduled_time(LocalDateTime scheduled_time) {
        this.scheduled_time = scheduled_time;
    }

    @Override
    public String toString() {
        return "CalendarEventDto{" +
                "name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", scheduled_time=" + scheduled_time +
                '}';
    }

    public Map<String, String> serialize() {
        Map<String, String> calendarEventDtoMap = new HashMap<>();
        calendarEventDtoMap.put("__class__", "model.calendar_event_dto.CalendarEventDTO");
        calendarEventDtoMap.put("name", this.name);
        calendarEventDtoMap.put("description", this.description);
        calendarEventDtoMap.put("scheduled_time", this.scheduled_time.toString());

        return calendarEventDtoMap;
    }
}
