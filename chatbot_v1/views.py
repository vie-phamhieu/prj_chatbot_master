from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Create your views here.

def home(request):
    return render(request, "index.html")

def get_bot_response(request):
    user_text = request.GET.get('msg', '')
    response = str(english_bot.get_response(user_text))
    return HttpResponse(response)