import urllib.request, urllib.parse

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return "ERR", str(e)

q = urllib.parse.quote("هارد 1 ترابایت")
tests = [
    ("digikala", "https://api.digikala.com/v1/search/?q=" + q),
    ("torob", "https://api.torob.com/v4/base-product/search/?page=0&size=10&query=" + q),
]
for name, url in tests:
    status, body = get(url)
    print("=====", name, status, len(body))
    print(body[:400])
