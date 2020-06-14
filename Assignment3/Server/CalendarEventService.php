<?php

require_once("CalendarEvent.php");
require_once("CalendarEventDto.php");
require_once("CalendarEventRepository.php");

class CalendarEventService
{
    public $calendarEventRepository;

    public function __construct()
    {
        $this->calendarEventRepository = new CalendarEventRepository();
    }

    public function persist($calendarEvent)
    {
        return $this->calendarEventRepository->persist($calendarEvent);
    }

    public function getAll()
    {
        return array_map("CalendarEventDto::fromCalendarEvent", $this->calendarEventRepository->getAll());
    }
}
