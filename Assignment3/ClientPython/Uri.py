def uriFields(uri):
#
# <protocol>:[//][<user>@]<[d:/]host>[:<port>][<path>][?<query>][#<fragment>]
# i1 ______ ^
# i2 ______ \___/
# i3 __________________ ^
# i4 _____________________ \___/
# i5 ________________________________ ^
# i6 _______________________________________ ^
# i6f start file as suffix on path
# i6t start type as suffix on file
# i7 ________________________________________________ ^
# i8 __________________________________________________________ ^
#
    port = {"ftp://":"21", "mailto:":"25", "http://":"80", "https://":"443", "rmi://":"1099"}
    res = {"protocol":"", "user":"", "host":"", "port":"", "path":"", "file":"", "type":"", "query":"", "fragment":""}
    i8 = uri.find("#")
    if i8 > 0:
        res["fragment"] = uri[i8 + 1:]
        uri = uri[:i8]
    i7 = uri.find("?")
    if i7 > 0:
        res["query"] = uri[i7 + 1:]
        uri = uri[:i7]
    i1 = uri.find(":")
    i2 = uri.find("://")
    if i2 > 0:
        res["protocol"] = uri[:i2 + 3]
    elif i1 > 0:
        res["protocol"] = uri[:i1 + 1]
    uri = uri[len(res["protocol"]):]
    i3 = uri.find("@")
    if i3 > 0:
        res["user"] = uri[:i3]
        uri = uri[len(res["user"]) + 1:]
    i4 = uri.find(":/")
    if i4 == 1:
        i5 = uri.find(":", 3)
        i6 = uri.find("/", 3)
    else:
        i5 = uri.find(":")
        i6 = uri.find("/")
    if i6 > 0:
        res["path"] = uri[i6 + 1:]
        uri = uri[:i6]
    if res["protocol"] in port:
        res["port"] = port[res["protocol"]]
    if i5 > 0:
        res["port"] = uri[i5 + 1:]
        uri = uri[:i5]
    res["host"] = uri
    uri = res["path"]
    i6f = uri.rfind("/") + 1
    uri = uri[i6f:]
    res["file"] = uri
    i6t = uri.rfind(".") + 1
    if i6t > 0:
        res["type"] = uri[i6t:]
    return res
"""
def main():
    uri = [\
        "http://www.ubbcluj.ro",\
        "http://www.ubbcluj.ro/cluj.html",\
        "http://www.scs.ubbcluj.ro:8080/calcul/index.jsp?nr1=50&sir1=Ceva&nr2=40",\
        "http://www.scs.ubbcluj.ro:8080/calcul/medie?nr1=50&sir1=Ceva&nr2=40",\
        "http://www.cs.ubbcluj.ro/~florin/SO/index.html#ultimul",\
        "http://en.wikipedia.org/wiki/URI#Examples_of_URI_references",\
        "file://d:/agenda/departament/fisier.h",\
        "file://home/cs/florin/Socket.pdf",\
        "ftp://ftp.netscape.com/pub/Linux/shell",\
        "mailto:pop@scs.ubbcluj.ro?subject=Test&body=Salut%oAtinere%20internaut",\
        "PYROLOC://localhost:7766/exec",\
        "PYRO:exec@localhost:7543",\
        "http://pop@www.scs.ubbcluj.ro:8080/calcul/index.jsp?nr1=50&sir1=Ceva&nr2=40#ultimul"]
    kRes = ["protocol","user","host","port","path","file","type","query","fragment"]
    for i in uri:
        print (i)
        res = uriFields(i)
        for j in kRes:
            print (j + "=" + res[j] + " "),
        print
        print
main()
"""
