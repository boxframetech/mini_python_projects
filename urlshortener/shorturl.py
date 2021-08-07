import pyshorteners

your_url = input('Please enter your url:...\n')

shortener = pyshorteners.Shortener()

shortened_url = shortener.tinyurl.short(your_url)

print("Your new short url is..: ", shortened_url)