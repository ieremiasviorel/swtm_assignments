<?php
function uriFields($uri) {
//
// <protocol>:[//][<user>@]<[d:/]host>[:<$port>][<path>][?<query>][#<fragment>]
// $i1 ______ ^
// $i2 ______ \___/
// $i3 __________________ ^
// $i4 _____________________ \___/
// $i5 ________________________________ ^
// $i6 _______________________________________ ^
// $i6f start file as suffix on path
// $i6t start type as suffix on file
// $i7 ________________________________________________ ^
// $i8 __________________________________________________________ ^
//
    $kPort = array("ftp://","mailto:","http://","https://","rmi://");
    $vPort = array("21",    "25",     "80",     "443",     "1099");
    $kRes = array("protocol","user","host","port","path","file","type","query","fragment");
    $port = array();
    $res = array();
    for ($i1 = 0; $i1 < count($kPort); $i1++)
        $port[$kPort[$i1]] = $vPort[$i1];
    for ($i1 = 0; $i1 < count($kRes); $i1++)
        $res[$kRes[$i1]] = "";
    if ($uri == null || strlen($uri) < 3)
        return $res;
    $i8 = strpos($uri, "#");           if (!$i8) $i8 = -1;
    if ($i8 > 0) {
        $res["fragment"] = substr($uri, $i8 + 1);
        $uri = substr($uri, 0, $i8);
    }
    $i7 = strpos($uri, "?");           if (!$i7) $i7 = -1;
    if ($i7 > 0) {
        $res["query"] = substr($uri, $i7 + 1);
        $uri = substr($uri, 0, $i7);
    }
    $i1 = strpos($uri, ":");           if (!$i1) $i1 = -1;
    $i2 = strpos($uri, "://");         if (!$i2) $i2 = -1;
    if ($i2 > 0)
        $res["protocol"] = substr($uri, 0, $i2 + 3);
    else if ($i1 > 0)
        $res["protocol"] = substr($uri, 0, $i1 + 1);
    $uri = substr($uri, strlen($res["protocol"]));
    $i3 = strpos($uri, "@");           if (!$i3) $i3 = -1;
    if ($i3 > 0) {
        $res["user"] = substr($uri, 0, $i3);
        $uri = substr($uri, strlen($res["user"]) + 1);
    }
    $i4 = strpos($uri, ":/");          if (!$i4) $i4 = -1;
    if ($i4 == 1) {
        $i5 = strpos($uri, ":", 3);
        $i6 = strpos($uri, "/", 3);
    } else {
        $i5 = strpos($uri, ":");
        $i6 = strpos($uri, "/");
    }
                                       if (!$i5) $i5 = -1;
                                       if (!$i6) $i6 = -1;
                                       if ($i6 > 0) {
        $res["path"] = substr($uri, $i6 + 1);
        $uri = substr($uri, 0, $i6);
    }
    if (array_key_exists($res["protocol"], $port))
        $res["port"] = $port[$res["protocol"]];
    if ($i5 > 0) {
        $res["port"] = substr($uri, $i5 + 1);
        $uri = substr($uri, 0, $i5);
    }
    $res["host"] = $uri;
    $uri = $res["path"];
    $i6f = strrpos($uri, "/");         if (!$i6f) $i6f = -1;
    $i6f++;
    $uri = substr($uri, $i6f);
    $res["file"] = $uri;
    $i6t = strrpos($uri, ".");         if (!$i6t) $i6t = -1;
    $i6t++;
    if ($i6t > 0)
        $res["type"] = substr($uri, $i6t);
    return $res;
}
/*
$uri = array (
        "http://www.ubbcluj.ro",
        "http://www.ubbcluj.ro/cluj.html",
        "http://www.scs.ubbcluj.ro:8080/calcul/index.jsp?nr1=50&sir1=Ceva&nr2=40",
        "http://www.scs.ubbcluj.ro:8080/calcul/medie?nr1=50&sir1=Ceva&nr2=40",
        "http://www.cs.ubbcluj.ro/~florin/SO/index.html#ultimul",
        "http://en.wikipedia.org/wiki/URI#Examples_of_URI_references",
        "file://d:/agenda/departament/fisier.h",
        "file://home/cs/florin/Socket.pdf",
        "ftp://ftp.netscape.com/pub/Linux/shell",
        "mailto:pop@scs.ubbcluj.ro?subject=Test&body=Salut%oAtinere%20internaut",
        "PYROLOC://localhost:7766/exec",
        "PYRO:exec@localhost:7543",
        "http://pop@www.scs.ubbcluj.ro:8080/calcul/index.jsp?nr1=50&sir1=Ceva&nr2=40#ultimul" );
$kRes = array("protocol","user","host","port","path","file","type","query","fragment");
for ($i = 0; $i < count($uri); $i++) {
    echo $uri[$i] . "\n";
    $res = uriFields($uri[$i]);
    for($j = 0; $j < count($kRes); $j++) {
        echo $kRes[$j] . "=" . $res[$kRes[$j]] . " ";
    }
    echo "\n";
    echo "\n";
}
*/
?>
