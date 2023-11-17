import requests
import os
data = [
    "https://skyscraperpage.com/diagrams/images/70344.gif",
    "https://skyscraperpage.com/diagrams/images/113373.gif",
    "https://skyscraperpage.com/diagrams/images/69357.gif",
    "https://skyscraperpage.com/diagrams/images/111151.gif",
    "https://skyscraperpage.com/diagrams/images/96684.gif",
    "https://skyscraperpage.com/diagrams/images/63497.gif",
    "https://skyscraperpage.com/diagrams/images/80251.gif",
    "https://skyscraperpage.com/diagrams/images/77926.gif",
    "https://skyscraperpage.com/diagrams/images/102012.gif",
    "https://skyscraperpage.com/diagrams/images/117078.gif",
    "https://skyscraperpage.com/diagrams/images/114145.gif",
    "https://skyscraperpage.com/diagrams/images/59735.gif",
    "https://skyscraperpage.com/diagrams/images/80333.gif",
    "https://skyscraperpage.com/diagrams/images/97496.gif",
    "https://skyscraperpage.com/diagrams/images/101982.gif",
    "https://skyscraperpage.com/diagrams/images/112704.gif",
    "https://skyscraperpage.com/diagrams/images/95708.gif",
    "https://skyscraperpage.com/diagrams/images/62733.gif",
    "https://skyscraperpage.com/diagrams/images/80214.gif",
    "https://skyscraperpage.com/diagrams/images/111443.gif",
    "https://skyscraperpage.com/diagrams/images/92785.gif",
    "https://skyscraperpage.com/diagrams/images/102193.gif",
    "https://skyscraperpage.com/diagrams/images/96774.gif",
    "https://skyscraperpage.com/diagrams/images/75959.gif",
    "https://skyscraperpage.com/diagrams/images/99458.gif"
]


# Ensure the 'images' directory exists
if not os.path.exists('images'):
    os.makedirs('images')

# Iterate over the URLs and download each one
for url in data:
    response = requests.get(url)

    # Get the file name by splitting the URL on the slash and taking the last segment
    file_name = url.split('/')[-1]

    # Open the file in write-binary mode and write the response content to it
    with open(os.path.join('images', file_name), 'wb') as file:
        file.write(response.content)
