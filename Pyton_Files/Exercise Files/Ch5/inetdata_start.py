#
# Example file for retrieving data from the internet
#

import urllib.request


def main():
    webUrl = urllib.request.urlopen("https://google.com")
    print("Result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()
