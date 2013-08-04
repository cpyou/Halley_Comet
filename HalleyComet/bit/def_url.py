#-*-coding:utf8-*-
from bit.models import Url
import hashlib

def long_to_short(long_url):
    if long_url[:4] != "http":
        long_url = "http://" + long_url

    db_url = Url.objects.filter(long_url__exact=long_url)
    if db_url:
        short_url = db_url[0].short_url
    else:
        short_url = hashlib.sha1(long_url).hexdigest()[:8]
        Url.objects.create(long_url=long_url, short_url=short_url)
    return short_url

def short_to_long(short_url):
    long_url = Url.objects.filter(short_url__exact=short_url)
    full_long_url = long_url[0].long_url
    return full_long_url
