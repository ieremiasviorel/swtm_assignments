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
        // Create connection
        $this->connection = mysqli_connect($this->serverName, $this->username, $this->password);

        // Check connection
        if (!$this->connection) {
            die("Connection failed: " . mysqli_connect_error());
        }
    }

    public function getById($id)
    {
        $sql = "SELECT id, name, description, scheduled_time FROM wsmt_xml_rpc_service.calendar_event WHERE id = '" . $id . "'";

        $result = $this->connection->query($sql);

        return $result->fetch_object("CalendarEvent");
    }
}
