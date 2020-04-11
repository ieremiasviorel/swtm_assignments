using System;
using System.Collections.Generic;

namespace ClientCS.model
{
    class CalendarEventDto
    {
        public string name { get; set; }
        public string description { get; set; }
        public DateTime scheduled_time { get; set; }

        public CalendarEventDto(String name, String description, DateTime scheduled_time)
        {
            this.name = name;
            this.description = description;
            this.scheduled_time = scheduled_time;
        }

        public static CalendarEventDto CalendarEventDtoFromDict(Object calendarEventDtoObj)
        {
            Dictionary<Object, Object> calendarEventDtoDict = (Dictionary<Object, Object>)calendarEventDtoObj;
            return new CalendarEventDto(
            (string)calendarEventDtoDict[(Object)"name"],
            (string)calendarEventDtoDict[(Object)"description"],
            Convert.ToDateTime((string)calendarEventDtoDict[(Object)"scheduled_time"]));
        }
    }
}
