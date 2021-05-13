from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import time
import random
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


    # Mentalízate de que te vas a hacer rico siendo un influencer.

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/?hl=es")
time.sleep(5)

username = browser.find_element_by_css_selector("[name='username']")
password = browser.find_element_by_css_selector("[name='password']")
login = browser.find_element_by_css_selector("button")

     # Pon tu nombre y contraseña.

username.send_keys("nombre")
password.send_keys("contraseña")
login.click()

time.sleep(4)

      # Selecciona los hastags en la variable lista_de_hastags, cada uno entre comillas y separados por coma.

lista_de_hastags = ['videogame', 'pc']

tag = -1

for hashtag in lista_de_hastags:
    tag += 1
    browser.get('https://www.instagram.com/explore/tags/'+ lista_de_hastags[tag] + '/')

    time.sleep(5)
    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    image_count = 0

    for picture in pictures:

           # Pon el número de publicaciones que quieres que recorra el bot para que le comente, le de like y le siga.

        if image_count >= 2:
            break

        picture.click()
        time.sleep(4)

           # Me gusta

        corazon = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
        corazon.click()
        time.sleep(2)

           # Configura el comentario a comentar :)

        def frase_random():
            muy = ("muy", "muuy", "muuuy", "muuuuy")
            fan = ("fan!!", "chulo :)", "guapo (:", "top!!!!!")
            num = random.randrange(0, 4)
            comentario = (muy[num] + ' ' + fan[num])
            return(comentario)

        try:
               if browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[3]/div").text == "Se han limitado los comentarios en esta publicación.":
                   pass
        except:
            cmt = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]")
            cmt.click()
            time.sleep(1)
            browser.find_element_by_xpath(
                "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(frase_random())
            time.sleep(3)
            browser.find_element_by_xpath(
                "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)
            time.sleep(4)

           # Follows. PON TU NOMBRE EN EL SEGUNDO IF QUE SINO SE ESTROPEA EL BOT AL VER UNA PUBLICACIÓN TUYA.

        if browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").text == 'Seguir':
            if browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text != 'skibidigamer':
                browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button").click()
        time.sleep(5)

           # Cerrar y pasar a la siguiente foto

        cerrar = browser.find_element_by_css_selector("[aria-label='Cerrar']")
        cerrar.click()

           # Tiempo que está entre publicación y publicación para que no te baneen de la bida. No puedes superar los 200 follows por hora.

        sleep(randint(20, 26))

        image_count += 1
        time.sleep(5)
