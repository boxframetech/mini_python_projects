import webbrowser as wb

def webauto():
    firefox = 'firefox'

    URLS = (
        "google.com",
        "gmail.com"
    )

    for url in URLS:
        print("opening :",url)
        wb.get(firefox).open(url)

webauto()