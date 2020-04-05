package com.swtm.pyro.assig;

import com.swtm.pyro.assig.cli.CommandLineInterface;
import com.swtm.pyro.assig.util.Uri;
import net.razorvine.pyro.PyroProxy;
import org.beryx.textio.TextIO;
import org.beryx.textio.TextIoFactory;
import org.beryx.textio.TextTerminal;

import java.io.IOException;
import java.util.Hashtable;

public class Main {

    public static PyroProxy startClient(String urlServ) throws IOException {
        Hashtable<String, String> uri = Uri.uriFields(urlServ);
        String server = uri.get("user");
        String host = uri.get("host");
        int port = Integer.parseInt(uri.get("port"));

        return new PyroProxy(host, port, server);
    }

    public static void main(String[] args) throws Exception {
        PyroProxy proxy;

        if (args.length > 0)
            proxy = startClient(args[0]);
        else
            proxy = startClient("PYRO:exec@localhost:7543");

        TextIO textInterface = TextIoFactory.getTextIO();
        TextTerminal textTerminal = textInterface.getTextTerminal();

        CommandLineInterface cli = new CommandLineInterface(proxy, textInterface, textTerminal);

        textTerminal.println("**********************************************");
        textTerminal.println("***  Welcome to Events Agenda Application  ***");
        textTerminal.println("**********************************************");

        cli.handleCliStart();

        proxy.close();
    }
}
