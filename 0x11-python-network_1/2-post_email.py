#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    value = {"email": mail}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')

    print(the_page)
