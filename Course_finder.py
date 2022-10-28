from bs4 import BeautifulSoup
from info_retriever import get_info
import requests
import csv
import threading
#from sshfs import SSHFileSystem


def get_courses(link):
    print(f'initializing Scraping from: {link}')
    site = requests.get(link)
    html = site.content

    # create the beautifulSoup object
    
    soup = BeautifulSoup(html,"html.parser")
    subjects = soup.find_all(class_='nostyle collection-product-card')
    
    courses=[]
    for i in range(len(subjects)):
        if "Course" in subjects[i].text:
            courses.append(subjects[i])
    
    #Multithreading the process to lower execution time.
    print('Progress: ')
    info_1=[]
    info_2=[]
    t1 = threading.Thread(target=multi_thread, args=(courses[0:len(courses)//2],info_1,"1",))
    t2 = threading.Thread(target=multi_thread, args=(courses[len(courses)//2:],info_2,"2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # Join both lists from threads
    info = info_1+info_2

    #csv file headers
    fields = ['Course Name', 'First Instructor Name', 'Course Description', '# of students enrolled', '# of ratings'] 

    #write to a csv file
    with open('Results.csv', 'w') as f:
        write = csv.writer(f)      
        write.writerow(fields)
        write.writerows(info)

    # sending file to the server
    # Connect with a password
    # !!!!normally this value shall be stored in .env file for securty for the needs of the porject .env file is not created
    #fs = SSHFileSystem(
    #    '127.0.0.1',
    #    username='90536',
    #    password='ayk12290'
    #)

def multi_thread(courses,info=[],thread=0):
    for i in range(len(courses)):
        link = f"https://www.coursera.org{courses[i]['href']}"
        print(f'thread {thread} progress is :',i+1,'/',len(courses))
        info.append(get_info(link=link))
    return info
