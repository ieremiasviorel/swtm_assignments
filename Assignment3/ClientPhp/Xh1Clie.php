<?php
require_once("xmlrpc/xmlrpc.inc");
require_once("Uri.php");
require_once("CalendarEvent.php");
require_once("CalendarEventRepository.php");
require_once("CalendarEventService.php");

class Xh1Clie
{
    function __construct($urlServ)
    {
        echo "Client PHP XML-RPC " . $urlServ . "<br/>";
        $uri = uriFields($urlServ);
        $pathServ = $uri["path"];
        if (strcasecmp($uri["type"], "php") == 0) {
            $pathServ = "";
            $proxy = new xmlrpc_client("http://" . $uri["host"] . ":" . $uri["port"] . "/" . $uri["path"]);
        } else {
            $pathServ .= ".";
            $proxy = new xmlrpc_client("http://" . $uri["host"] . ":" . $uri["port"] . "/");
        }

        $message = new xmlrpcmsg($pathServ . "ping");
        $response = $proxy->send($message);
        $response = php_xmlrpc_decode($response->value());
        echo "ping: " . $response . "<br/>";

        $message = new xmlrpcmsg($pathServ . "upcase", array(new xmlrpcval("negru", "string")));
        $response = $proxy->send($message);
        $response = php_xmlrpc_decode($response->value());
        echo "upcase: negru = " . $response . "<br/>";

        $message = new xmlrpcmsg($pathServ . "add", array(new xmlrpcval("66", "int"), new xmlrpcval("75", "int")));
        $response = $proxy->send($message);
        $response = php_xmlrpc_decode($response->value());
        echo "add: 66 + 75 = " . $response . "<br/>";

        echo "<br/>";

        echo "EVENTS LIST <br/>";
        $message = new xmlrpcmsg($pathServ . "events_list");
        $response = $proxy->send($message);
        $response = php_xmlrpc_decode($response->value(), array("decode_php_objs"));
        foreach ($response as $obj) {
            echo $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br/>";
        }

        echo "EVENT ADD <br/>";
        $message = new xmlrpcmsg($pathServ . "event_add", array(
            new xmlrpcval("Name", "string"),
            new xmlrpcval("Description", "string"),
            new xmlrpcval("2020-01-01 12:00:00", "string")
        ));
        // $response = $proxy->send($message);
        // $response = php_xmlrpc_decode($response->value());
        // echo $response;
    }
}

echo "Local debug <br/>";
$calendarEventService = new CalendarEventService();
$events = $calendarEventService->getAll();
foreach ($events as $obj) {
    echo $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br/>";
}

echo "<br/>";

$events = $calendarEventService->getByNamePartial("1");
foreach ($events as $obj) {
    echo $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br/>";
}

echo "<br/>";

$events = $calendarEventService->getByDescriptionPartial("desc");
foreach ($events as $obj) {
    echo $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br/>";
}

echo "<br/>";

$events = $calendarEventService->edit("a", "ab", "aabb", "2020-10-10 16:00:00");
foreach ($events as $obj) {
    echo $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br/>";
}

echo "<br/><br/>";

if (isset($_GET["urlServ"]))
    new Xh1Clie($_GET["urlServ"]);
else
    new Xh1Clie("http://localhost/Xh1Serv.php");
