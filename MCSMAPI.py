import http.client
import pickle as p

def protected_instance(address,port,type,uuid,remote_uuid,apikey):
    conn = http.client.HTTPConnection(address, port)
    payload = ''
    headers = {}
    conn.request("PUT", "/api/protected_instance/{type}?uuid={uuid}&remote_uuid={remote_uuid}&apikey={apikey}".format(type=type,uuid=uuid,remote_uuid=remote_uuid,apikey=apikey), payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    if data.decode("utf-8")[status] == 200 :
        return OK
    if data.decode("utf-8")[status] != 200:
        return data.decode("utf-8")

if __name__ == "__main__":
    with open(".\server_list.pkl","rb") as server_list:
        server = p.load(server_list)
    protected_instance(server[survival][address],server[survival][port],"restart",server[survival][uuid],server[survival][remote_uuid],server[survival][apikey])