from flask import Flask, render_template_string, request
from pytube import YouTube
import os
import requests
import traceback

# pip3 install flask
# pip3 install pytube
# replace the link variable with youtube link
# replace path variable with the path to save video

# from pytube import StreamQuery
# from pytube import Stream
# from pytube import Playlist
# from pytube import CaptionQuery
# from pytube import Caption
# from pytube import Search


app = Flask("__name__")

# @app.route('/')
@app.route('/dart')
def main():
    from flask import Markup
    if request.method == 'POST':
        link = request.
        link = "https://www.youtube.com/watch?v=H5v3kku4y6Q"
        try:
            path = "/Users/muralikrishna/Desktop/test"
            dot = "."
            extension = "mp4"
            ytObj = YouTube(link)
            title = ytObj.title

            status = isinstance(ytObj.check_availability(), type(None))
            if(status):
                final_name = title + dot + extension
                yt= YouTube(link)
                yt.streams.get_by_resolution("360p").download(path,final_name)
            else:
                print("Video is not Available")
        except:
            print("Connection Error")  # to handle exception
            traceback.print_exc()
        return "Video is successfully downloaded."
        # return render_template_string('<h1>Voila! Platform is ready to used</h1>')


def getVideoResolution(ytObj):
    availableResolutions = list()
    for stream in ytObj.streams:
        if isinstance(stream.resolution, type(None)):
            pass
        else:
            resolution = stream.resolution
            resolution = int(resolution[:len(resolution) - 1])  # removing p in resolution
            if (resolution not in availableResolutions):
                availableResolutions.append(resolution)
            else:
                pass
    availableResolutions.sort(reverse=True)
    return availableResolutions

def getImage(url):
    page = requests.get(url)
    f_ext = os.path.splitext(url)[-1]
    f_name = 'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)

def installPrerequisites():
    pass
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    installPrerequisites()
    app.debug = True
    app.run(host='127.0.0.1',port=1729)

