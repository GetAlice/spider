import http.cookiejar
import urllib.parse
import urllib.request


filename = 'cookie.txt'
cookie_jar = http.cookiejar.MozillaCookieJar(filename)

handle = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handle)