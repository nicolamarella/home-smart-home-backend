import requests
import json
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
    requests.post(
        BACKEND_URL+"events",
        headers=headers,
        json=data_to_send
    )
    pass


def test():
    notify_server(True)


if __name__ == "__main__":
    test()
