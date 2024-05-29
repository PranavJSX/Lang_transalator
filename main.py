import  requests


def detect(mystring):
    import requests

    url = "https://google-translator9.p.rapidapi.com/v2/detect"

    payload = {"q": mystring}
    headers = {
        "x-rapidapi-key": "48a6801135msh0b3a132a1d0ed8fp1d9938jsnb7cfe0e4a2b4",
        "x-rapidapi-host": "google-translator9.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return ((response.json())['data']['detections'][0][0]['language'])

def translate(mystring,target):
    import requests

    url = "https://google-translator9.p.rapidapi.com/v2"

    payload = {
        "q": mystring,
        "source" : detect(mystring),
        "target" : target,
        "format" : 'text'
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "48a6801135msh0b3a132a1d0ed8fp1d9938jsnb7cfe0e4a2b4",
        "X-RapidAPI-Host": "google-translator9.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())

def getlangs():
    url = "https://translate.googleapis.com/v3beta1/{parent=projects/1}/supportedLanguages"
    print(requests.get(url))


if __name__ == '__main__':
    mystring = input()
    target = input()
    translate(mystring,target)
    # getlangs()

