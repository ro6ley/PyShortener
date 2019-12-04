# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import argparse
import requests
from requests.exceptions import ConnectionError
import json


def shorten_url(url):
    """ Function that receives a URL and sends it to SHorte.st API
    """
    try:
        response = requests.put("https://api.shorte.st/v1/data/url",
                                 {"urlToShorten": url},
                                 headers={"public-api-token": "TOKEN_GOES_HERE"})

        api_response = json.loads(response.content)

        return {"status": api_response['status'],
                "shortenedUrl": api_response['shortenedUrl'],
                "message": "URL shortened successfully"}
        
    except ConnectionError:
        return {"status": "error",
                "shortenedUrl": None,
                "message": "Please ensure you are connected to the internet and try again."}
    except Exception as e:
        return {"status": "error",
                "shortenedUrl": None,
                "message": "We ran into an error processing your URL. Try again later"}


def handle_output(result):
    """ Function to format and print the output
    """
    if result["status"] == "ok":
        print(f"{result['message']}. Your shortened url is:\n"
              f"\t{result['shortenedUrl']}")
    elif result["status"] == "error":
        print(f"{result['message']}")


# create a parser
parser = argparse.ArgumentParser(description='Shorten URLs on the terminal')

# add argument
parser.add_argument('--url',
                    default="google.com",
                    help="The URL to be shortened")

args = vars(parser.parse_args())

if args.get('url'):
    result = shorten_url(args['url'])
    handle_output(result)
