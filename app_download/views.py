# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
from pathlib import Path
 
 
# defining function
def home(request):
 
    # checking whether request.method is post or not
    if request.method == 'POST':
       
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
 
        # setting video resolution
        stream = video.streams.get_lowest_resolution()
         
        # downloads video
        stream.download(output_path=Path.home() / 'Downloads')
 
        # returning HTML page
        return render(request, 'app_download/home.html')
    return render(request, 'app_download/home.html')
