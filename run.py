from remote import RemoteIntegrate
from local import OracleDatabase

remote = RemoteIntegrate()

for d in remote.get_pending():

    package = []

    db = OracleDatabase(
        d['sqlConnection']['connectionString'],
        d['sqlConnection']['user'],
        d['sqlConnection']['password']
        )
    
    for i in db.get_cursor(d['sqlQuery'], []):
        print(i)

    #print("Sending -> ", d['code'], ", Status -> ", remote.send_data(package))
    print("Sending -> ", d)