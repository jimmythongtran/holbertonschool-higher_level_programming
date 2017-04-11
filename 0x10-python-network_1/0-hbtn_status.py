#!/usr/bin/python3
"""
this script fetches https://intranet.hbtn.io/status using urllib
"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("    - type:", type(html))
    print("    - content:", html)
    print("    - utf8 content:", html.decode("utf8"))
