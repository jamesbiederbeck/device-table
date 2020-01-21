from requests_html import HTMLSession
import bs4
from pprint import pprint

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def getHostNamesFromRouter():
    session = HTMLSession()
    r = session.get('https://10.0.0.1', verify=False)
    foo = r.html.xpath('//*[@id="internet-usage"]/table')[0]
    hosts = []
    for row in foo.xpath("//tr")[1:]: #skip header
        host = {}
        host["host_name"],host["mac_address"],host["connection"] = row.text.splitlines()
        hosts.append(host)
    print(f"Found {len(hosts)} hosts")
    pprint(hosts)
    return jsonify(hosts)

if __name__ == "__main__":
    app.run(debug=True)