import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.

    Args:
    - subreddit (str): The subreddit to query.

    Returns:
    - int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    user_agent = {'User-Agent': 'owen20108'}  # Set a custom User-Agent to avoid issues

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print(f"Error accessing subreddit '{subreddit}': HTTP status code {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = number_of_subscribers(subreddit)
        print(result)

