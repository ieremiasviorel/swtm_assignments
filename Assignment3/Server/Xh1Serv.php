<?php
require_once("xmlrpc/xmlrpc.inc");
require_once("xmlrpc/xmlrpcs.inc");
require_once("CalendarEvent.php");
require_once("CalendarEventRepository.php");

class Xh1Serv
{
        public $calendarEventRepository;

        public function __construct()
        {
                $this->calendarEventRepository = new CalendarEventRepository();
        }

        function ping()
        {
                return new xmlrpcresp(new xmlrpcval(
                        "PHP XML-RPC " . $_SERVER["SERVER_NAME"] . " (" .
                                gethostbyname($_SERVER["SERVER_NAME"]) . ":" .
                                $_SERVER["SERVER_PORT"] . "), " . date("Y.m.d H:i:s"),
                        "string"
                ));
        }

        function upcase($msg)
        {
                $s = php_xmlrpc_decode($msg->params[0]);
                return new xmlrpcresp(new xmlrpcval(strtoupper($s), "string"));
        }

        function add($msg)
        {
                $a = php_xmlrpc_decode($msg->params[0]);
                $b = php_xmlrpc_decode($msg->params[1]);
                return new xmlrpcresp(new xmlrpcval($a + $b, "int"));
        }

        function events_list()
        {
                $calendarEvents = $this->calendarEventRepository->getAll();
                $calendarEventsVal = php_xmlrpc_encode($calendarEvents, array("encode_php_objs"));
                return new xmlrpcresp($calendarEventsVal);
        }

        function start()
        {
                $serv = new xmlrpc_server(
                        array(
                                "ping" =>
                                array(
                                        "function" => "Xh1Serv::ping",
                                        "signature" => array(array("string"))
                                ),
                                "upcase" =>
                                array(
                                        "function" => "Xh1Serv::upcase",
                                        "signature" => array(array("string", "string"))
                                ),
                                "add" =>
                                array(
                                        "function" => "Xh1Serv::add",
                                        "signature" => array(array("int", "int", "int"))
                                ),
                                "events_list" =>
                                array(
                                        "function" => array($this, "events_list"),
                                        "signature" => array(array("string"))
                                ),
                        ),
                        false
                );
                $serv->service();
        }
}

$serviciu = new Xh1Serv();
$serviciu->start();
