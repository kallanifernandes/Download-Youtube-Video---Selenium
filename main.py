<<<<<<< HEAD
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from yt_dlp import YoutubeDL
import time

driver = webdriver.Chrome()
=======
'''from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
>>>>>>> 458fd61bf226087f652c48568c4f15b5ca46c393
driver.get("https://imersaopowerbi.com/dataflix-aula-02/")

time.sleep(5)

play_btn = driver.find_element(By.CLASS_NAME, "elementor-custom-embed-play")
play_btn.click()

time.sleep(5)

get_iframe = driver.find_element(By.TAG_NAME, "iframe")
yt_url = get_iframe.get_attribute("src")

clean_link = yt_url.split('?')[0].replace("embed/", "watch?v=")
<<<<<<< HEAD
print("Link do youube: ", clean_link)

driver.quit()

#yt = YouTube(clean_link)
#stream = yt.streams.get_highest_resolution()
#stream.download(output_path='.', filename="aula02")

yr_dlp ={
  'outtmpl' : 'aula02.%(ext)s',
  'format' : 'bestvideo+bestaudio/best', 
  'merge_output_format' : 'mp4',
  'quiet' : False
}
with YoutubeDL(yr_dlp) as ydl:
  ydl.download([clean_link])
=======

print("Link do youtube: ", clean_link)

driver.quit()

yt = YouTube(clean_link)
stream = yt.streams.get_highest_resolution()
stream.download(output_path=".", filename="Aula02")
'''



'''#INDIVIDUAL, JOGA O LINK E BAIXA
from pytube import YouTube

yt_url = "https://www.youtube.com/watch?v=381xJVcTpuk"

yt = YouTube(yt_url)

stream = yt.streams.get_highest_resolution()
stream.download(output_path='.', filename="Aula02")
print('Donwnloado concluido')'''




'''#SCRIPT PARA LIMPAR CODIGO
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def limpar_link(link):
    # Corrige link embed ou encurtado
    if "embed/" in link:
        link = link.split("embed/")[-1].split("?")[0]
        link = f"https://www.youtube.com/watch?v={link}"
    return link

try:
    link = input("Cole o link do vídeo: ").strip()
    link_corrigido = limpar_link(link)
    print(f"Link corrigido: {link_corrigido}")

    yt = YouTube(link_corrigido)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=".", filename="Aula02")
    print("Download concluído com sucesso!")

except Exception as e:
    print("Ocorreu um erro:")
    print(e)
'''
>>>>>>> 458fd61bf226087f652c48568c4f15b5ca46c393
