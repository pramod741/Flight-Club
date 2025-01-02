import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d7be849242479fb1abd586e4afe9bfd8/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d7be849242479fb1abd586e4afe9bfd8/flightDeals/users"

header = {
    'Authorization': 'your_authorization_id'
}

class DataManager:

    def __init__(self):
        # self._user = os.environ.get("SHEETY_USERNAME")
        # self._password = os.environ["SHEETY_PASSWORD"]
        self._user = "your_user_name"
        self._password = "your_password"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = []

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)

    def get_users_data(self):
        response = requests.get(SHEETY_USERS_ENDPOINT, headers=header)
        self.customer_data = [row['whatIsYourEmail?'] for row in response.json()['users']]

