#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as exeptionA:
        print('Error code: {}'.format(exeptionA.code))
