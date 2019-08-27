#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays value"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
