import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url='http://gmail.com/'


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags=soup('h1')

for tag in tags:
    print(tag)
