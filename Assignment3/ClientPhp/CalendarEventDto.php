<?php

require_once("CalendarEvent.php");

class CalendarEventDto
{
    public $name;
    public $description;
    public $scheduled_time;

    public static function fromCalendarEvent($calendarEvent)
    {
        return CalendarEventDto::fromValues(
            $calendarEvent->name,
            $calendarEvent->description,
            $calendarEvent->scheduled_time
        );
    }

    public static function fromValues($name, $description, $scheduled_time)
    {
        $calendarEventDto = new CalendarEventDto();
        $calendarEventDto->name = $name;
        $calendarEventDto->description = $description;
        $calendarEventDto->scheduled_time = $scheduled_time;

        return $calendarEventDto;
    }
}
