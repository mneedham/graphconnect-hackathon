import requests
import csv

from bs4 import BeautifulSoup
from soupselect import select

page = open("constituencies.html", 'r')
soup = BeautifulSoup(page.read())

REQUIRED_INDICES = [0,3,4]

with open("constituencies.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    for row in select(soup, "table.wikitable tr"):
        if select(row, "th"):
            # print [cell.text for cell in select(row, "th")]
            output = [x[1].text for x in enumerate(select(row, "th")) if x[0] in REQUIRED_INDICES]
            print output
            writer.writerow(output)

        if select(row, "td"):
            output = [x[1].text.encode("utf-8") for x in enumerate(select(row, "td")) if x[0] in REQUIRED_INDICES]
            print output
            writer.writerow(output)
