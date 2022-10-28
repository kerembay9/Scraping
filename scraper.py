from bs4 import BeautifulSoup
import requests

def get_categories():
    site = requests.get('https://www.coursera.org/browse/')
    html = site.content


    soup = BeautifulSoup(html,"html.parser")
    Subjects = soup.find_all(class_='topic-image')
    links=[]
    for i in range(len(Subjects)):
        links.append("https://www.coursera.org"+ Subjects[i].parent['data-track-href'])

    return links
