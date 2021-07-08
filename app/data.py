import requests;

auth = {
    "user": "admin",
    "password": "district"
}


def get_json(url, auth):
    user = auth['user'];
    password = auth['password']

    r = requests.get(url, auth=(user, password))
    return r.json()


data_elements_url = "https://play.dhis2.org/2.34.6/api/dataElements"
data_elements = get_json(data_elements_url, auth)['dataElements']

print(data_elements)
