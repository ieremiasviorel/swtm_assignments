<?php

require_once("CalendarEvent.php");

class CalendarEventRepository
{
    public $serverName = "localhost";
    public $username = "root";
    public $password = "";
    public $connection = null;

    public function __construct()
    {
        $this->connection = mysqli_connect($this->serverName, $this->username, $this->password);

        if (!$this->connection) {
            die("Connection failed: " . mysqli_connect_error());
        }
    }

    public function getAll()
    {
        $sqlQuery = "SELECT id, name, description, scheduled_time FROM wsmt_xml_rpc_service.calendar_event ORDER BY scheduled_time ASC";

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

    public function getById($id)
    {
        $sql = "SELECT id, name, description, scheduled_time FROM wsmt_xml_rpc_service.calendar_event WHERE id = '" . $id . "'";

        $result = $this->connection->query($sql);

        return $result->fetch_object("CalendarEvent");
    }
}
