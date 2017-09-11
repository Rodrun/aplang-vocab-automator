import requests
from bs4 import BeautifulSoup


def get_definition(search):
    """
    Get the first definition of the word using merriam-webster dictionary online.
    :param search: Word to find the definition of.
    :return: Definition of search.
    """
    # Read HTML website
    req = requests.get("https://merriam-webster.com/dictionary/" + search)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    elems = soup.select('p[class="definition-inner-item with-sense"] > span')
    if len(elems) == 0:
        elems = soup.select('p[class="definition-inner-item"] > span')
    return elems[0]


path = input("File: ")
# Read and store into list
with open(path) as f:
    content = f.readlines()
f.close()

for element in content:
    word = element[:element.find(":")]
    print(word + "\t" + str.lstrip(get_definition(word).text).split(":")[1])
