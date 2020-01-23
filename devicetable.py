import sys
import warnings
from pprint import pprint
from requests_html import HTMLSession
import bs4
from flask import Flask, render_template, request, jsonify

#todo add cert verification outside requests
warnings.filterwarnings(
        'ignore',
        message="Unverified HTTPS request is being made. Adding certificate verification is strongly advised."
                        )

app = Flask(__name__)

@app.route("/")
def main():
    hosts = getHostNamesFromRouter()
    #only return json string if we're running in flask
    if "scan" not in sys.argv:
        return jsonify(hosts)

def getHostNamesFromRouter():
    session = HTMLSession()
    r = session.get('https://10.0.0.1', verify=False)
    data = r.html.xpath('//*[@id="internet-usage"]/table')[0]
    hosts = []
    for row in data.xpath("//tr")[1:]: #skip header
        host = {}
        host["host_name"],host["mac_address"],host["connection"] = row.text.splitlines()
        hosts.append(host)
    print(f"Found {len(hosts)} hosts")
    pprint(hosts)
    return hosts

if __name__ == "__main__":
    if "scan" in sys.argv:
        getHostNamesFromRouter()
    else:
        app.run(debug=True)
    