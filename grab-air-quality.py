import os
import sys
from bs4 import BeautifulSoup
from urllib import urlopen

base_url = "http://aqsdr1.epa.gov/aqsweb/aqstmp/airdata"

page = urlopen("%s/%s" % (base_url, "/download_files.html")).read()
doc = BeautifulSoup(page, "lxml")
raw_data_table = doc.select("#Raw")[0].find_next("table")

for row in raw_data_table.find_all("tr"):
    year = None
    for item in row.find_all("td"):
        if item.find("a") is None:
            year = item.find("em").text
            continue

        data_file = item.find("a").get('href')
        url = "%s/%s" % (base_url, data_file)
        print("Downloading %s" % url)

        os.system("curl -o %s %s" % (os.path.join(".", "data", data_file), url))
#        sys.exit(0)
