# Author: Janne Keipert
# TODO: Login HPI
# TODO: Gather Sourcecode

from selenium import webdriver
import os
from datetime import date, timedelta
import docx
import progressbar
import Informations
from time import sleep

today = date.today()

options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome(options=options)
browser.get("https://www.hpi-schul-cloud.de/login")
listLinks = []

def login(): # Login into the Cloud
    print("Logging in")
    loginName = browser.find_element_by_xpath('//*[@id="name"]')
    loginKey = browser.find_element_by_xpath('//*[@id="password"]')
    submit = browser.find_element_by_xpath('//*[@id="submit-login"]')

    loginName.send_keys(Informations.hpiEmail)
    loginKey.send_keys(Informations.hpiPassword)
    submit.submit()
    if browser.current_url == "https://hpi-schul-cloud.de/dashboard":
        return True
    else:
        return False

def scrap(): # Gather the needed Information
    print("Starting Scrapping")
    listExercisesObj = browser.find_element_by_xpath('//*[@id="main-content"]/section[2]/div[2]')
    listExercisesList = listExercisesObj.text.split('\n')
    listExercisesOrdered = []
    listObjectsLinks = browser.find_elements_by_class_name("homework-link")
    for i in listObjectsLinks:
        listLinks.append(i.get_attribute("href"))
    for i in range(int((len(listExercisesList)-1) / 3)):
        listExercisesOrdered.append([listExercisesList[i * 3 + 2], listExercisesList[i * 3], listExercisesList[i * 3 + 1]])
    return listExercisesOrdered

def writeFile(listExercises): # Write the Informations in the File
    count = 0
    os.system('shutdown /s /t 999 /c "Du hast ' + str(len(listExercises)) + ' neue Aufgaben"')
    sleep(10)
    os.system('shutdown /a')
    with progressbar.ProgressBar(max_value=len(listExercises), enable_colors=False) as bar:
        listText = ["\n"]
        for i in listExercises:
            date = i[2].split()
            date = date[1]
            if date == "Abgabedatum" or date == "einem":
                pass
            else:
                subject = i[1].replace(" ", "").replace("10.4", "").replace("-", "").replace("Cordes", "").replace("fürden10.Jahrgang" ,"")
                exercise = i[0].replace(" ", "_").replace("10.4", "").replace("-", "").replace(",", "")
                dateExercise = today + timedelta(days=int(date))
                dateExercise = str(dateExercise).replace(" ", "").replace(".", "")
                fileWriteExercise = "Aufgaben/" + subject + "/" + dateExercise + "_" + exercise + ".docx"
                os.makedirs(os.path.dirname(fileWriteExercise), exist_ok=True)
                browser.get(listLinks[count])
                elementInstpect = browser.find_element_by_xpath('//*[@id="extended"]/div[1]/div[1]/div')

                textExercise = elementInstpect.text
                doc = docx.Document()
                doc.add_paragraph(textExercise)
                doc.add_paragraph(listLinks[count])
                listText.append("Aufgabe: " + exercise + " Fach: " + subject + " Abgabe: " + dateExercise)
                for ii in browser.find_elements_by_xpath('//*[@id="extended"]/div[1]/div[2]/ul/li/a'):
                    doc.add_paragraph(ii.get_attribute("href"))
                    print(ii.get_attribute("href"))
                if not (os.path.isfile(fileWriteExercise)):
                    doc.save(fileWriteExercise)
            bar.update(count)
            count += 1
        for i in listText:
            print(i)
        browser.quit()

if login():
    print("Succesfull Login")
    listExercices = scrap()
    writeFile(listExercices)
    input("Succesfully Finished press Enter to quit")
else:
    print("Du hast eine falsche EMail adresse oder Passwort angegeben")
    browser.quit()
