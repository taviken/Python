import requests
import bs4
from bs4 import BeautifulSoup
from collections import namedtuple

episode = namedtuple("episode", ["title", "description"])

api_key = "qcwvczi99p8mu74mrkwbsp5eq"

if 1:
    url = r"https://mdblist.com/show/tt5171438/season/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    }
    page = requests.get(url, headers)

    soup = BeautifulSoup(page.content, "html.parser")


def extract_containers(soup):
    return soup.find_all("div", class_="eleven wide column")


def extract_episode_info(containers: bs4.element.ResultSet):
    episodes = []
    for container in containers:
        title = container.find("h4", class_="description")

        ep = episode(title.text)

        episodes.append(ep)
