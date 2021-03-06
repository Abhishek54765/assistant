# importing requests package
import requests


def indian_science():
    # BBC news api
    main_url = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c0b8a463407747acadbfe3dfd8c68085"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()
    print(open_bbc_page)

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)


# Driver Code
if __name__ == '__main__':
    # function call
    indian_science()
