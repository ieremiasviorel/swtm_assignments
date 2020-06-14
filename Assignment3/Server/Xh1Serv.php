<?php
require_once("xmlrpc/xmlrpc.inc");
require_once("xmlrpc/xmlrpcs.inc");
require_once("CalendarEvent.php");
require_once("CalendarEventRepository.php");
require_once("CalendarEventService.php");

class Xh1Serv
{
        public $calendarEventService;

        public function __construct()
        {
                $this->calendarEventService = new CalendarEventService();
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
                $calendarEvents = $this->calendarEventService->getAll();
                $calendarEventsVal = php_xmlrpc_encode($calendarEvents, array("encode_php_objs"));
                return new xmlrpcresp($calendarEventsVal);
        }

        function events_list_by_name($msg)
        {
                $calendarEventNamePartial =  php_xmlrpc_decode($msg->params[0]);
                $calendarEvents = $this->calendarEventService->getByNamePartial($calendarEventNamePartial);
                $calendarEventsVal = php_xmlrpc_encode($calendarEvents, array("encode_php_objs"));
                return new xmlrpcresp($calendarEventsVal);
        }

        function events_list_by_description($msg)
        {
                $calendarEventDescriptionPartial =  php_xmlrpc_decode($msg->params[0]);
                $calendarEvents = $this->calendarEventService->getByDescriptionPartial($calendarEventDescriptionPartial);
                $calendarEventsVal = php_xmlrpc_encode($calendarEvents, array("encode_php_objs"));
                return new xmlrpcresp($calendarEventsVal);
        }

        function event_add($msg)
        {
                $calendarEventName = php_xmlrpc_decode($msg->params[0]);
                $calendarEventDescription = php_xmlrpc_decode($msg->params[1]);
                $calendarEventScheduledTime = php_xmlrpc_decode($msg->params[2]);

                $calendarEvent = CalendarEvent::fromValues(
                        $calendarEventName,
                        $calendarEventDescription,
                        $calendarEventScheduledTime
                );

                $operationStatus = $this->calendarEventService->persist($calendarEvent);

                return new xmlrpcresp(new xmlrpcval($operationStatus, "boolean"));
        }

        function event_edit($msg)
        {
                $originalName = php_xmlrpc_decode($msg->params[0]);
                $updatedName = php_xmlrpc_decode($msg->params[1]);
                $updatedDescription = php_xmlrpc_decode($msg->params[2]);
                $updatedScheduledTime = php_xmlrpc_decode($msg->params[3]);

                $operationStatus = $this->calendarEventService->edit($originalName, $updatedName, $updatedDescription, $updatedScheduledTime);

                return new xmlrpcresp(new xmlrpcval($operationStatus, "boolean"));
        }

        function event_delete($msg)
        {
                $calendarEventName = php_xmlrpc_decode($msg->params[0]);

                $operationStatus = $this->calendarEventService->delete($calendarEventName);

                return new xmlrpcresp(new xmlrpcval($operationStatus, "boolean"));
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
                                "events_list_by_name" =>
                                array(
                                        "function" => array($this, "events_list_by_name"),
                                        "signature" => array(array("string", "string"))
                                ),
                                "events_list_by_description" =>
                                array(
                                        "function" => array($this, "events_list_by_description"),
                                        "signature" => array(array("string", "string"))
                                ),
                                "event_add" =>
                                array(
                                        "function" => array($this, "event_add"),
                                        "signature" => array(array("boolean", "string", "string", "string"))
                                ),
                                "event_edit" =>
                                array(
                                        "function" => array($this, "event_edit"),
                                        "signature" => array(array("boolean", "string", "string", "string", "string"))
                                ),
                                "event_delete" =>
                                array(
                                        "function" => array($this, "event_delete"),
                                        "signature" => array(array("boolean", "string"))
                                ),
                        ),
                        false
                );
                $serv->service();
        }
}

$serviciu = new Xh1Serv();
$serviciu->start();
