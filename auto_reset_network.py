# pip install huawei-lte-api

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

from time import sleep

from pprint import pprint

def reset_4G(client):
    # Set tp 2G
    net_mode = client.net.net_mode()
    client.net.set_net_mode(net_mode['LTEBand'],
                        net_mode['NetworkBand'],
                        "01")
    sleep(1)
    # Set tp 4G
    client.net.set_net_mode(net_mode['LTEBand'],
                            net_mode['NetworkBand'],
                            "03")
    sleep(1)

user = "admin"
password = "admin123"
ip = "192.168.0.1"

while True:
    try :
        url = "http://" + user + ":" + password + "@" + ip
        connection = AuthorizedConnection(url)
        client = Client(connection)

        while True:
            plmn = client.net.current_plmn()
            # print(plmn)
            if(plmn == "FAILED" or plmn['Rat'] != '7'):
                print("Reseting 4G")
                reset_4G(client)

            # print("Ok")
            sleep(5)

    except Exception as e :
        print("Connection error - " + str(e))
        sleep(10)