from django.shortcuts import render 
from django.core.files.base import ContentFile


import openai, os,requests
import json

from imagegenai.models import Image


from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY",None)
# Create your views here.
# Create your views here.

def generate_image_from_text(request):
    
    obj = None
    if api_key is not None and request.method =='POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
 
        response = openai.Image.create(

           prompt=user_input,
           size = "256x256" ,#512x512 1024x1024
        
        )
         
        print(response)
        
        img_url = response["data"][0]["url"]
        
        response = requests.get(img_url)
       
        print(response)
        img_file = ContentFile(response.content)
        
        count = Image.objects.count() + 1
        fname = f"image-{count}.jpg"
        
        obj = Image(phrase=user_input)
        obj.ai_image.save(fname,img_file)
        obj.save()
         
    
    return render(request,"imagegenai/image.html",{"object": obj})

