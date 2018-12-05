from remote import RemoteIntegrate
from local import OracleDatabase

remote = RemoteIntegrate()

for d in remote.get_pending():

    try:

        db = OracleDatabase(
            d['sqlConnection']['connectionString'],
            d['sqlConnection']['user'],
            d['sqlConnection']['password']
            )

        cursor = db.get_cursor(d['sqlQuery'], [])
        column_names = [row[0] for row in cursor.description]

        print("Query -> ", d['sqlQuery'])
        
        for c in cursor:
            # Montar a requisição
            package = []
            request = dict()
            request['code'] = d['code']
            request['data'] = list()
            data = {k : v for k, v in zip(column_names, c)}
            request['data'].append(data)
            package.append(request)
            success = remote.send_data(package)
            if success == False:
                print("Error Sending -> ", d['code'], ", Package -> ", package)

    except:
        print("Error on query ->", d['sqlQuery'])