# 0x16. API advanced

## General Objectives:bulb:
*How to read API documentation to find the endpoints you’re looking for
*How to use an API with pagination
*How to parse JSON results from an API
*How to make a recursive API call
*How to sort a dictionary by value

## Task's description:

### [0-subs](./0-subs.py)
* Function that queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is given, the function should return 0.
  * Requirements:
    * Prototype: def number_of_subscribers(subreddit)
    * If not a valid subreddit, return ```0```.
    * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
### [1-top ten](./1-top_ten.py)
* Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
  * Requirements:
    * Prototype: ```def top_ten(subreddit)```
    * If not a valid subreddit, print ```None```.
    * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
### [2-recurse](./2-recurse.py)
* Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
  * Requirements:
    * Prototype: ```def recurse(subreddit, hot_list=[])```
    * Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a    starting value in the main.
    * If not a valid subreddit, return ```None```.
    * NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
## Author
* **Juan Manuel Ramírez Saa** - [Juan8bits](https://github.com/Juan8bits)
