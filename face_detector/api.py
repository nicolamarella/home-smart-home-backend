import requests
import json
import sys
from pudb import set_trace
BACKEND_URL = 'http://131.159.209.35:8085/'
headers = {
    'Content-type': 'application/json',
}


def notify_server(user_is_asleep):
    """
    Notifies the server about a change of state in the user sleep condition
    """
    data_to_send = {
        "event_type": "asleep",
        "value": user_is_asleep
    }
    response = requests.post(
        BACKEND_URL+"events/",
        headers=headers,
        json=data_to_send
    )
    print(response)
    print(response.content)
    pass


def test(value):
    notify_server(value)


if __name__ == "__main__":
    wrong_usage = False
    if len(sys.argv)<2:
        wrong_usage = True
    try:
        value = int(sys.argv[1])
        assert value == 1 or value == 0
        bool_val = value > 0
    except:
        wrong_usage = True
    if wrong_usage:
        print("USAGE: python {} [0|1]".format(__file__))
    else:
        test(bool_val)
