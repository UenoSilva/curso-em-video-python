import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://uenosilva.github.io/laterplay/')
except urllib.request.URLError:
    print('\033[0;31mSite off\033[m')
else:
    print('\033[0;33mSite on\033[m')

