def getcs():
    Server=raw_input("Enter Server name:")
    Database=raw_input("Enter DB name:")
    Username=raw_input("Enter User name:")
    Password=raw_input("Enter Password:")
    cs="Servername=%s;Database=%s;Username=%s;Password=%s" % (Server, Database, Username, Password)
    return cs
def cstodict(cs):
    d={}
    for i in cs.split(";"):
        k,v = i.split("=")
        d[k] =v
    return d

cs=getcs()
print cstodict(cs)

