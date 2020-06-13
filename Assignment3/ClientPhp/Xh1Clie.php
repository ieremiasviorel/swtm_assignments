<?php
require_once("xmlrpc/xmlrpc.inc");
require_once("Uri.php");
require_once("CalendarEvent.php");
require_once("CalendarEventRepository.php");

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

        $message = new xmlrpcmsg($pathServ . "events_list");
        $response = $proxy->send($message);
        $response = php_xmlrpc_decode($response->value(), array("decode_php_objs"));
        foreach($response as $obj) {
            echo $obj->id . " | " . $obj->name . " | " . $obj->description . " | " . $obj->scheduled_time . "<br>";
        }
    }
}

if (isset($_GET["urlServ"]))
    new Xh1Clie($_GET["urlServ"]);
else
    new Xh1Clie("http://localhost/Xh1Serv.php");
