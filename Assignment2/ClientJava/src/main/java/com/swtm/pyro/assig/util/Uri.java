package com.swtm.pyro.assig.util;

import java.util.Hashtable;

public class Uri {
    public static Hashtable<String, String> uriFields(String uri) {
        //
        // <protocol>:[//][<user>@]<[d:/]host>[:<port>][<path>][?<query>][#<fragment>]
        // i1 ______ ^
        // i2 ______ \___/
        // i3 __________________ ^
        // i4 _____________________ \___/
        // i5 ________________________________ ^
        // i6 _______________________________________ ^
        // i6f start file as suffix on path
        // i6t start type as suffix on file
        // i7 ________________________________________________ ^
        // i8 __________________________________________________________ ^
        //
        int i1, i2, i3, i4, i5, i6, i6f, i6t, i7, i8;
        final String[] kPort = {"ftp://", "mailto:", "http://", "https://", "rmi://"};
        final String[] vPort = {"21", "25", "80", "443", "1099"};
        final String[] kRes = {"protocol", "user", "host", "port", "path", "file", "type", "query", "fragment"};
        Hashtable<String, String> port = new Hashtable<String, String>();
        Hashtable<String, String> res = new Hashtable<String, String>();
        for (i1 = 0; i1 < kPort.length; i1++)
            port.put(kPort[i1], vPort[i1]);
        for (i1 = 0; i1 < kRes.length; i1++)
            res.put(kRes[i1], "");
        if (uri == null || uri.length() < 3)
            return res;
        i8 = uri.indexOf("#");
        if (i8 > 0) {
            res.put("fragment", uri.substring(i8 + 1));
            uri = uri.substring(0, i8);
        }
        i7 = uri.indexOf("?");
        if (i7 > 0) {
            res.put("query", uri.substring(i7 + 1));
            uri = uri.substring(0, i7);
        }
        i1 = uri.indexOf(":");
        i2 = uri.indexOf("://");
        if (i2 > 0)
            res.put("protocol", uri.substring(0, i2 + 3));
        else if (i1 > 0)
            res.put("protocol", uri.substring(0, i1 + 1));
        uri = uri.substring(res.get("protocol").length());
        i3 = uri.indexOf("@");
        if (i3 > 0) {
            res.put("user", uri.substring(0, i3));
            uri = uri.substring(res.get("user").length() + 1);
        }
        i4 = uri.indexOf(":/");
        if (i4 == 1) {
            i5 = uri.indexOf(":", 3);
            i6 = uri.indexOf("/", 3);
        } else {
            i5 = uri.indexOf(":");
            i6 = uri.indexOf("/");
        }
        if (i6 > 0) {
            res.put("path", uri.substring(i6 + 1));
            uri = uri.substring(0, i6);
        }
        if (port.containsKey(res.get("protocol")))
            res.put("port", port.get(res.get("protocol")));
        if (i5 > 0) {
            res.put("port", uri.substring(i5 + 1));
            uri = uri.substring(0, i5);
        }
        res.put("host", uri);
        uri = res.get("path");
        i6f = uri.lastIndexOf("/") + 1;
        uri = uri.substring(i6f);
        res.put("file", uri);
        i6t = uri.lastIndexOf(".") + 1;
        if (i6t > 0)
            res.put("type", uri.substring(i6t));
        return res;
    }
/*
    public static void main(String args[]) {
        String[] uri = {
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
            "http://pop@www.scs.ubbcluj.ro:8080/calcul/index.jsp?nr1=50&sir1=Ceva&nr2=40#ultimul" };
        final String[] kRes = {"protocol","user","host","port","path","file","type","query","fragment"};
        for (int i = 0; i < uri.length; i++) {
            System.out.println(uri[i]);
            Hashtable res = uriFields(uri[i]);
            for(int j = 0; j < kRes.length; j++) {
                System.out.print(kRes[j] + "=" + res.get(kRes[j]) + " " );
            }
            System.out.println();
            System.out.println();
        }
    }
*/
}
