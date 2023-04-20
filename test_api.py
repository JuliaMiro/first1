import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
STATUS_OK = 200
AUTH_URL = "https://restful-booker.herokuapp.com/auth"

@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "Jimmy",
        "lastname": "Brownee",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code == 200
    yield booking_id




def test_get_all_bookings():
    response = requests.get(BASE_URL)
    print(f'\n{len(response.json())}')
    assert response.status_code == 200
    headers = ('Connection', 'keep-alive')
    assert headers in response.headers.items()
    # print(f"\n{response.headers}")
    # print(response.json())

def test_get_booking_with_id():
    response = requests.get(f"{BASE_URL}/1")
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice']
    assert response_data["firstname"] == "Sally"
    for key in expected_keys:
        assert key in response_data.keys()
    print(f"\n {response_data}")

def test_create_booking():
    payload = {
        "firstname": "Jimmy",
        "lastname": "Brownee",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code ==200
    response_get = requests.get(f'{BASE_URL}/{booking_id}')
    assert response_get.status_code == 200
    assert payload['firstname'] in response_get.json().values()


def test_create_booking_fix(booking_id)
    response= requests.get(f'{BASE_URL}/{booking_id}')
    assert response.status_code == 200
    assert response.json()['firstname'] == "Jimmy"

def test_user_autorization():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    # response_data = response.json()
    # print(response_data)
    response_data = response.json()
    assert response.status_code == STATUS_OK
    assert "token" in response_data

# update не писала 8 лекция 1.20.00 (время)
# delete 8 лекция c 1.34.00 не делала тоже

