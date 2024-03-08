#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid or there is an issue, it returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'by u/owen20108'}  # Set a custom User-Agent to avoid issues

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
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

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        
        if num_subscribers != 0:
            print(f"The subreddit '{subreddit}' has {num_subscribers} subscribers.")
        else:
            print(f"Unable to retrieve the number of subscribers for subreddit '{subreddit}'.")

