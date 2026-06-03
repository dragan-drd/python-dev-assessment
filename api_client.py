import requests


class Geo:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class Address:
    def __init__(self, street, suite, city, zipcode, geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = Geo(**geo)


class Company:
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catch_phrase = catchPhrase
        self.bs = bs


class User:
    def __init__(self, id, name, username, email, address, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = Address(**address)
        self.phone = phone
        self.website = website
        self.company = Company(**company)

    def print_info(self):
        print(self.name)
        print(self.email)
        print(self.address.city)


url = "https://jsonplaceholder.typicode.com/users"


def fetch_and_display_users(num_users):

    try:
        response = requests.get(url)
        response.raise_for_status()
        user_data_list = response.json()
    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP ERROR: {http_error}")
        return None
    except requests.exceptions.RequestException as request_error:
        print(f"NETWORK ERROR OCCURED: {request_error}")
        return None
    except ValueError:
        print(f"ERROR: response was not valid. {ValueError}")
        return None

    user_object_list = []

    for user_data_dict in user_data_list:
        try:
            temp = User(**user_data_dict)
            user_object_list.append(temp)
        except (TypeError, KeyError) as json_error:
            print(
                f"JSON STRUCTURE UNEXPECTED OR MISSING, SKIPPING RECORD. ERROR: {json_error}"
            )
            continue

    if len(user_object_list) == 0:
        print("NO USERS TO DISPLAY")
        return None

    counter = 0
    for user in user_object_list:
        user.print_info()
        print("\n")
        counter += 1
        if counter == num_users:
            break

    if len(user_data_list) < num_users:
        print(f"{num_users} users requested, but only {len(user_data_list)} exist")

    return user_object_list


result1 = fetch_and_display_users(4)
print("-------------------------------------------")
result2 = fetch_and_display_users(16)
