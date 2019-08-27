#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status"""
import sys
import requests

if __name__ == "__main__":
    cont = requests.get(argv[1])
    print(cont.headers.get('X-Request-Id'))
