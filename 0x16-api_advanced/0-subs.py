#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    # Send the GET request
    response = get(url, headers=user_agent)
    
    # Check the HTTP status code
    if response.status_code == 200:
        try:
            # Parse the JSON data
            results = response.json()
            return results.get('data').get('subscribers')
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return 0
    elif response.status_code == 404:
        print(f"Error: Subreddit '{subreddit}' not found.")
        return 0
    elif response.status_code == 403:
        print(f"Error: Access to subreddit '{subreddit}' is forbidden.")
        return 0
    else:
        print(f"Error accessing subreddit '{subreddit}': HTTP status code {response.status_code}")
        return 0

if __name__ == "__main__":
    # Test the function with command-line argument
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

