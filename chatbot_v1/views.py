from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, "index.html")

def call_flask_api(request):
    try:
        # Gửi yêu cầu GET đến API Flask
        response = requests.get('https://khf7bsyelj.execute-api.ap-southeast-1.amazonaws.com/chatbot')
        # Xử lý dữ liệu từ response nếu cần
        data = response.json()
        # Trả về dữ liệu từ API Flask dưới dạng JSON
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        # Xử lý các trường hợp lỗi khi gọi API Flask
        return JsonResponse({'error': str(e)}, status=500)
