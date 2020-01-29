import requests
import logging

logging.getLogger().setLevel(logging.DEBUG)

URL = "https://api.github.com/repos/mozilla/geckodriver/releases"

try:
    req = requests.get(URL)
except Exception as e:
    logging.error("Cannot connect to Github API")

print(" ".join([release["tag_name"] for release in req.json()]))
