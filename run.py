import cx_Oracle
from remote import RemoteIntegrate

remote = RemoteIntegrate()

for d in remote.get_pending():
    package = []
    package.append(d)
    print("Sending -> ", d['code'], ", Status -> ", remote.send_data(package))