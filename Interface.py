import PySimpleGUI as sg
from scraper import get_categories
from Course_finder import get_courses

#Get Coursera categories first
scraped_category_list=get_categories()

#define menu items from categories above
button_menu_def = [' Scraped Categories', [scraped_category_list]]

#selected tag specifies what will be written on the button
selected=scraped_category_list[0]

layout = [
# This part is in case server credentials are asked as input 
#[[sg.Text('Please enter the server adress:')],[sg.Input('')]], 

[sg.ButtonMenu('Start Scraping:', menu_def=button_menu_def)],
[sg.Button(f'Press to Scrape: {selected}', key='-BUTTON-')]]
layout_2 = [
[sg.Text('Scraping in Progress... Please Wait')]]
window =sg.Window('Web Scraping Tool',layout,size=(650, 450))

while True:
    event,values=window.read()
    try:
        print(values[event])
    except:
        pass
    if event in (sg.WIN_CLOSED, 'Exit'):
            break
    elif event =='-BUTTON-':
        link=selected
        sg.popup('Scraping will start when ok button is pressed. Check The terminal for progress')
        window.close()
        get_courses(link)
        break
        
    for i in range(len(scraped_category_list)):
        if scraped_category_list[i] == values[event]:
                selected = scraped_category_list[i]
                window['-BUTTON-'].update(f'Press to Scrape: {values[event]}')
    
