from bs4 import BeautifulSoup
import requests
def get_info(link):
    site = requests.get(link)
    html = site.content
    soup = BeautifulSoup(html,"html.parser")

    #find course name from the h1 tag 
    Course = soup.find("h1")
    Course_name =Course.text

    #find instructor name from class name
    First_instructor = soup.find(class_='rc-BannerInstructorInfo rc-BannerInstructorInfo__seo-experiment')
    
    #None.span returns error. To prevent try except used.
    try:            
        if First_instructor.span.span is not None:
            First_instructor_name=First_instructor.span.text.replace(First_instructor.span.span.text, '')
        else:
            First_instructor_name=First_instructor.span.text
    except:
        First_instructor_name= "Not entered"
    
    try:
        Course_description=soup.find(class_='description').text
    except:
        Course_description="Unavailable"
    #None.children returns error. To prevent try except used.
    try:
        Enrolled = soup.find(class_='_1fpiay2').children
        Enrolled_count = list(list(Enrolled)[0].children)[0].text
    except:
        Enrolled_count="unknown"

    #None[0].text returns error. To prevent try except used.    
    try:
        Rating = soup.select("[data-test='ratings-count-without-asterisks']")
        Rate=Rating[0].text[:-8]
    except:
        Rate="unavailable"
        
    return [ Course_name, First_instructor_name,Course_description ,Enrolled_count,Rate]
