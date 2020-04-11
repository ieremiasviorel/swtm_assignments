using System;
using System.Collections;

namespace ClientCS.util
{
    public static class Uri
    {
        public static Hashtable uriFields(String uri)
        {
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
            String[] kPort = { "ftp://", "mailto:", "http://", "https://", "rmi://" };
            String[] vPort = { "21", "25", "80", "443", "1099" };
            String[] kRes = { "protocol", "user", "host", "port", "path", "file", "type", "query", "fragment" };
            Hashtable port = new Hashtable();
            Hashtable res = new Hashtable();
            for (i1 = 0; i1 < kPort.Length; i1++)
                port.Add(kPort[i1], vPort[i1]);
            for (i1 = 0; i1 < kRes.Length; i1++)
                res.Add(kRes[i1], "");
            if (uri == null || uri.Length < 3)
                return res;
            i8 = uri.IndexOf("#");
            if (i8 > 0)
            {
                res["fragment"] = uri.Substring(i8 + 1);
                uri = uri.Substring(0, i8);
            }
            i7 = uri.IndexOf("?");
            if (i7 > 0)
            {
                res["query"] = uri.Substring(i7 + 1);
                uri = uri.Substring(0, i7);
            }
            i1 = uri.IndexOf(":");
            i2 = uri.IndexOf("://");
            if (i2 > 0)
                res["protocol"] = uri.Substring(0, i2 + 3);
            else if (i1 > 0)
                res["protocol"] = uri.Substring(0, i1 + 1);
            uri = uri.Substring(((String)res["protocol"]).Length);
            i3 = uri.IndexOf("@");
            if (i3 > 0)
            {
                res["user"] = uri.Substring(0, i3);
                uri = uri.Substring(((String)res["user"]).Length + 1);
            }
            i4 = uri.IndexOf(":/");
            if (i4 == 1)
            {
                i5 = uri.IndexOf(":", 3);
                i6 = uri.IndexOf("/", 3);
            }
            else
            {
                i5 = uri.IndexOf(":");
                i6 = uri.IndexOf("/");
            }
            if (i6 > 0)
            {
                res["path"] = uri.Substring(i6 + 1);
                uri = uri.Substring(0, i6);
            }
            if (port.ContainsKey(res["protocol"]))
                res["port"] = port[res["protocol"]];
            if (i5 > 0)
            {
                res["port"] = uri.Substring(i5 + 1);
                uri = uri.Substring(0, i5);
            }
            res["host"] = uri;
            uri = (String)res["path"];
            i6f = uri.LastIndexOf("/") + 1;
            uri = uri.Substring(i6f);
            res["file"] = uri;
            i6t = uri.LastIndexOf(".") + 1;
            if (i6t > 0)
                res["type"] = uri.Substring(i6t);
            return res;
        }
        /*
            public static void Main(String[] args) {
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
                String[] kRes = {"protocol","user","host","port","path","file","type","query","fragment"};
                for (int i = 0; i < uri.Length; i++) {
                    Console.WriteLine(uri[i]);
                    Hashtable res = uriFields(uri[i]);
                    for(int j = 0; j < kRes.Length; j++) {
                        Console.Write(kRes[j] + "=" + res[kRes[j]] + " " );
                    }
                    Console.WriteLine();
                    Console.WriteLine();
                }
            }
        */
    }
}
