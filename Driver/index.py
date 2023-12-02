from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


service = Service("Driver/chromedriver.exe")
#Para abrirlo en incognito a ver si me funciona con la publicidad fija
chrome_options= Options()
chrome_options.add_argument('--incognito')
bot = webdriver.Chrome(service=service, options=chrome_options)
bot.maximize_window()
time.sleep(1)

#Aca se abre la pagina.
bot.get("https://www.viajesexito.com")
time.sleep(5)
#Spoiler: no lo logro y toca cerrarla manualmente y ahora ya no pasa de pestaña a la de viajes
#oferta = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
#oferta.click()
time.sleep(1)
viajes = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a/p')
time.sleep(2)
viajes.click()
time.sleep(2)

#Salida
Ciudad_salida = bot.find_element(By.NAME, 'popUpCityPredictiveFrom_netactica_air' )
Ciudad_salida.click()
Ciudad_salida.send_keys("Jose Maria Cordova")
time.sleep(5)

#Destino
Ciudad_destino = bot.find_element(By.XPATH, '/html/body/form/section[2]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/input')
Ciudad_destino.click()
Ciudad_destino.send_keys("Punta cana")
time.sleep(5)

#Calendario
Calendar_ = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input')
Calendar_.click()
Calendar_.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[1]/div[2]/div[1]')
Calendar_.click()

Calendar_out = bot.find_element(By.XPATH. '/html/body/div[8]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]')
Calendar_out.click()
accept = bot.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[2]/button[2]')

#Rooms
Room = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
Room.click()
addRoom = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]/button[1]')
addRoom.click()
acceptRoom=bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/button')
acceptRoom.click()

Search = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[4]/a/p')
Search.click()


#Precios
precio = bot.find_elements(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div')

print("Precios de los paquetes en la primera página:")
    for precio in precios:
        print(precio.text)
        
bot.quit()
