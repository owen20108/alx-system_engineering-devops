import requests
from sys import argv

def number_of_subscribers(subreddit):
    user_agent = {'User-Agent': 'owen20108'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    response = requests.get(url, headers=user_agent)

    # Check the response status code
    if response.status_code == 200:
        try:
            # Parse the JSON data
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return 0
    else:
        print(f"Error accessing subreddit '{subreddit}': HTTP status code {response.status_code}")
        return 0

if __name__ == "__main__":
    subreddit = argv[1] if len(argv) > 1 else None

    if subreddit:
        result = number_of_subscribers(subreddit)
        print(f"The subreddit '{subreddit}' has {result} subscribers.")
    else:
        print("Please pass an argument for the subreddit to search.")

