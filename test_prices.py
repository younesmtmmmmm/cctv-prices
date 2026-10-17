import urllib.request, urllib.parse, urllib.error, json

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None

opener = urllib.request.build_opener(NoRedirect)

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    try:
        with opener.open(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace"), ""
    except urllib.error.HTTPError as e:
        return e.code, "", e.headers.get("Location", "")
    except Exception as e:
        return "ERR", str(e), ""

q = urllib.parse.quote("هارد اینترنال 1 ترابایت")

print("===== digikala")
s, b, loc = get("https://api.digikala.com/v1/search/?q=" + q)
print(s, len(b), "Location:", loc)
print(b[:300])

print("===== torob")
s, b, loc = get("https://api.torob.com/v4/base-product/search/?page=0&size=10&q=" + q)
print(s, len(b))
try:
    data = json.loads(b)
    for r in data.get("results", [])[:6]:
        print(r.get("name1"), "|", r.get("price"), "|", r.get("price_text"), "|", r.get("shop_text"))
    if data.get("results"):
        print("KEYS:", list(data["results"][0].keys()))
except Exception as e:
    print("parse error", e)
    print(b[:300])
