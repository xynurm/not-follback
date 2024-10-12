import requests

# Replace with your GitHub username
username = 'your-username'
token = 'your-personal-access-token'

def get_followers():
    url = f'https://api.github.com/users/{username}/followers'
    response = requests.get(url, auth=(username, token))
    return [user['login'] for user in response.json()]

def get_following():
    url = f'https://api.github.com/users/{username}/following'
    response = requests.get(url, auth=(username, token))
    return [user['login'] for user in response.json()]

followers = set(get_followers())
following = set(get_following())

# People you are following who are not following you back
not_following_back = following - followers

print("People who did not follow back:")
for user in not_following_back:
    print(user)
