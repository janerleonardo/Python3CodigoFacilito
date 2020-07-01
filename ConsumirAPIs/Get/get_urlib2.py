from urllib.request  import urlopen #urllib2 se a dividdo en python 3 con los  nombres urllib.request y urllib.error.

if __name__=='__main__':
    response = urlopen('https://www.google.com.co/').read()
    print(response)


