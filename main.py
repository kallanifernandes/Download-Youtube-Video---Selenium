from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from yt_dlp import YoutubeDL
import time

driver = webdriver.Chrome()
driver.get("https://imersaopowerbi.com/dataflix-aula-02/")

time.sleep(5)

play_btn = driver.find_element(By.CLASS_NAME, "elementor-custom-embed-play")
play_btn.click()

time.sleep(5)

get_iframe = driver.find_element(By.TAG_NAME, "iframe")
yt_url = get_iframe.get_attribute("src")

clean_link = yt_url.split('?')[0].replace("embed/", "watch?v=")
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
