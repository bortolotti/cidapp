from remote import RemoteIntegrate
from local import OracleDatabase

remote = RemoteIntegrate()

for d in remote.get_pending():

    package = []

    try:

        db = OracleDatabase(
            d['sqlConnection']['connectionString'],
            d['sqlConnection']['user'],
            d['sqlConnection']['password']
            )

        cursor = db.get_cursor(d['sqlQuery'], [])
        column_names = [row[0] for row in cursor.description]
        
        for c in cursor:
            data = [{k : v } for k, v in zip(column_names, c)]
            print(data)
            

        #print("Sending -> ", d['code'], ", Status -> ", remote.send_data(package))
        #print("Sending -> ", d)

    except:
        print("Error on query ->", d['sqlQuery'])