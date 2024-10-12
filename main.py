import requests

# Replace with your GitHub username
username = 'your-username'
token = 'your-personal-access-token'

following_url = f'https://api.github.com/users/{username}/following'
followers_url = f'https://api.github.com/users/{username}/followers'

def get_user_list(url):
    users = []
    while url:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            users.extend(user['login'] for user in response.json())
            # Check if there is a next page
            url = response.links.get('next', {}).get('url')
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            break
    return users

# Get lists of followers and following
following = get_user_list(following_url)
followers = get_user_list(followers_url)

# Find users who are not following back
not_following_back = [user for user in following if user not in followers]

# Display the results
print("Users not following you back:")
for user in not_following_back:
    print(user)

print(f"Total non-followers: {len(not_following_back)}")
