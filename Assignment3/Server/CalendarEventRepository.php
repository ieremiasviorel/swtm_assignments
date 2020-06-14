<?php

require_once("CalendarEvent.php");

class CalendarEventRepository
{
    public $serverName = "localhost";
    public $username = "root";
    public $password = "";
    public $tableName = "wsmt_xml_rpc_service.calendar_event";
    public $connection = null;

    public function __construct()
    {
        $this->connection = mysqli_connect($this->serverName, $this->username, $this->password);

        if (!$this->connection) {
            die("Connection failed: " . mysqli_connect_error());
        }
    }

    public function persist($calendarEvent)
    {
        $sql = "INSERT INTO " . $this->tableName . " (name, description, scheduled_time) VALUES (
            '" . $calendarEvent->name . "',
            '" . $calendarEvent->description . "',
            '" . $calendarEvent->scheduled_time . "');";

        if ($this->connection->query($sql) === TRUE) {
            return true;
        } else {
            return false;
        }
    }

    public function getAll()
    {
        $sqlQuery = "SELECT id, name, description, scheduled_time FROM " . $this->tableName . " ORDER BY scheduled_time ASC;";

        $sqlResult = $this->connection->query($sqlQuery);

        $result = array();

        if ($sqlResult != null) {
            while ($obj = $sqlResult->fetch_object("CalendarEvent")) {
                array_push($result, $obj);
            }
            $sqlResult->free_result();
        }

        return $result;
    }
}
