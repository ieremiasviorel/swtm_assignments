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

    public function edit($originalName, $updatedName, $updatedDescription, $updatedScheduledTime)
    {
        return $this->calendarEventRepository->edit($originalName, $updatedName, $updatedDescription, $updatedScheduledTime);
    }

    public function delete($calendarEventName) 
    {
        return $this->calendarEventRepository->delete($calendarEventName);
    }

    public function getAll()
    {
        return array_map("CalendarEventDto::fromCalendarEvent", $this->calendarEventRepository->getAll());
    }

    public function getByNamePartial($calendarEventNamePartial) 
    {
        return $this->calendarEventRepository->getByNamePartial($calendarEventNamePartial);
    }

    public function getByDescriptionPartial($calendarEventDescriptionPartial) 
    {
        return $this->calendarEventRepository->getByDescriptionPartial($calendarEventDescriptionPartial);
    }
}
