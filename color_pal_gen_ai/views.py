from django.shortcuts import render 


import openai, os
import json

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY",None)
# Create your views here.

def chatbot(request):
    
    chatbot_response = None
    if api_key is not None and request.method =='POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt=user_input
        response = openai.Completion.create(
            engine="text-davinci-003",
           # prompt = prompt, 
           #prompt="Answer as a crazy man: ",
          # prompt=f"Translate the text in spanish: {user_input} " ,
           prompt=f"If the question is realted to weather - answer it: {user_input}, else say: i cannot answer it ",
            max_tokens=256,
           # stop= "."
           temperature = 0.5
        )
        
        print(response)
        chatbot_response = response["choices"][0]["text"]
    return render(request, 'color_pal_gen_ai/color.html',{"response":chatbot_response})





