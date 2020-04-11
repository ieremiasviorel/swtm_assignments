using System;
using System.Collections;
using ClientCS.cli;
using Razorvine.Pyro;

namespace ClientCS
{
    class Program
    {
        static PyroProxy StartClient(String urlServ)
        {
            Console.WriteLine("Client C# Pyro (pyrolite): " + urlServ);
            Hashtable uri = util.Uri.uriFields(urlServ);
            String server = (String)uri["user"];
            String host = (String)uri["host"];
            int port = int.Parse((String)uri["port"]);

            return new PyroProxy(host, port, server);
        }

        static void Main(string[] args)
        {
            PyroProxy proxy;

            if (args.Length > 0)
                proxy = StartClient(args[0]);
            else
                proxy = StartClient("PYRO:exec@localhost:7543");

            Console.WriteLine("**********************************************");
            Console.WriteLine("***  Welcome to Events Agenda Application  ***");
            Console.WriteLine("**********************************************");

            CommandLineInterface cli = new CommandLineInterface(proxy);

            cli.HandleCliStart();

            proxy.close();

        }
    }
}
