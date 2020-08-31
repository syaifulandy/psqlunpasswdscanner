import psycopg2
import ipaddress

ListScan=''
listunpasswdpostgre =[]
net=ipaddress.ip_network(ListScan)
for i in net:
    try:
           con = psycopg2.connect(database="postgres", user="postgres",
                                  password="", host=i,
                                  port="5432",connect_timeout=1)
           print ("SUCCESS!!!!!!! IP ",i, "PSQL Version", con.server_version)
           found = str(i) +" PSQL Version "+ str(con.server_version)
           listunpasswdpostgre.append(str(found))
    except psycopg2.DatabaseError as e:
           print ("failed",i)
           print (e)


print("List IP with Unpasswd PostgreSQL Vulnerability:")
if len(listunpasswdpostgre)==0:
    print ("Not Found")
elif len(listunpasswdpostgre)>0:
    for x in range (len(listunpasswdpostgre)):
        print (listunpasswdpostgre[x])

