import requests


def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user = data["data"]
        username = user["login"]["username"]
        country = user["location"]["country"]
        return user, username, country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        user, username, country = fetch_random_user()
        print(f"Username: {username}")
        print(f"Country: {country}")
        print(user)
    except Exception as e:
        print(str(e))
        return


if __name__ == "__main__":
    main()
