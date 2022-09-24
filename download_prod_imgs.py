import requests

urls = """https://cdn.theyes.com/images/v2/162b01f788501c13bfa1ef4a61872333.jpg
https://cdn.theyes.com/images/v2/f5e6a118c55d6f3d4b00f173da8a5a4a.jpg
https://cdn.theyes.com/images/v2/48144eca8695d1ca39043ed110d3f36a.jpg
https://cdn.theyes.com/images/v2/380d8521c94f13ea89716228b347a002.jpg
https://cdn.theyes.com/images/v2/974f8b0a9eb6000d5e033e82ce5b9d22.jpg
https://cdn.theyes.com/images/v2/33f58d6d474b9885ec9020839471b1b3.jpg
https://cdn.theyes.com/images/v2/0e4556fd8bbbd821768d9bc3590847ed.jpg
https://cdn.theyes.com/images/v2/c9d5604e65a7ff2e780296ad14fadd25.jpg
https://cdn.theyes.com/images/v2/4d68696f4c8a9a6137ce54254a4e7983.jpg
https://cdn.theyes.com/images/v2/1d128c97d15bdcbbbe271e71b2110786.jpg"""
urls = urls.split('\n')


for idx, url in enumerate(urls):
    print(idx, url)
    r = requests.get(url)
    with open(f"{idx}.jpg", 'wb') as outfile:
        outfile.write(r.content)