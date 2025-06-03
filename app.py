from pytubefix import YouTube
from flask import Flask, request, render_template
from pytubefix.cli import on_progress

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gera_yt():
  message = ''

  if request.method == 'POST':
      url = request.form['url']

      try:
         yt = YouTube(url)
         titulo = yt.title
         sepIndex = titulo.split()
         nameArq = f"{sepIndex[0]}_{sepIndex[1]}_video.mp4"
         ys = yt.streams.get_highest_resolution()
         ys.download(filename=nameArq)

         message = "Video baixando com sucesso"

      
      except Exception as e: 
         message = f'Erro: {e}'

  return render_template('index.html', message=message)

# Faz o app rodar quando o script é executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração (útil para testes)


#url = "https://www.youtube.com/watch?v=puymQ31SgG0"

#yt = YouTube(url, on_progress_callback=on_progress)
#print(yt.title)

#ys = yt.streams.get_highest_resolution()
#ys = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

#ys.download(output_path='.', filename="video_youtube.mp4")