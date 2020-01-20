from requests_html import HTMLSession
import bs4
from pprint import pprint

def getHostNamesFromRouter():
    session = HTMLSession()
    r = session.get('https://10.0.0.1', verify=False)
    foo = r.html.xpath('//*[@id="internet-usage"]/table')[0]
    hosts = []
    for row in foo.xpath("//tr"):
        host = {}
        host["host_name"],host["mac_address"],host["connection"] = row.text.splitlines()
        hosts.append(host)
    print(f"Found {len(hosts)} hosts")
    pprint(hosts)
    return hosts

if __name__ == "__main__":
    getHostNamesFromRouter()