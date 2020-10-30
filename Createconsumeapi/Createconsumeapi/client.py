import requests

def get_data():
    url='http://127.0.0.1:8000/Show'
    response = requests.get(url)
    cust_data = response.json()
    for e in cust_data:
        print(e)
get_data()