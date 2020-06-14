<?php

require_once("CalendarEventDto.php");

class CalendarEvent
{
    public $id;
    public $name;
    public $description;
    public $scheduled_time;

    public static function fromCalendarEventDto($calendarEventDto)
    {
        return CalendarEvent::fromValues(
            $calendarEventDto->name,
            $calendarEventDto->description,
            $calendarEventDto->scheduled_time
        );
    }

    public static function fromValues($name, $description, $scheduled_time)
    {
        $calendarEvent = new CalendarEvent();
        $calendarEvent->name = $name;
        $calendarEvent->description = $description;
        $calendarEvent->scheduled_time = $scheduled_time;

        return $calendarEvent;
    }
}
